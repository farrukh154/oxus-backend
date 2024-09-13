IF OBJECT_ID('abacus_disbursement') IS NOT NULL
    DROP FUNCTION abacus_disbursement
GO

CREATE FUNCTION abacus_disbursement
(	
	@dateFrom datetime,
	@dateTo datetime,
	@currencyFilter char(300),
	@branchFilter char(300)
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT *,
	case when PreparedData.Sector=N'Савдо' then 'Trade'
	else case when PreparedData.Sector=N'Растанипарварӣ' then 'Horticulture'
	else case when PreparedData.Sector=N'Истеҳсолот' then 'Production'
	else case when PreparedData.Sector=N'Истеъмолот' then 'Consumer'
	else case when PreparedData.Sector=N'Чорвопарварӣ' then 'Livestock'
	else case when PreparedData.Sector=N'Хизматрасонӣ' then 'Service'
	else case when PreparedData.Sector=N'Ғайраҳо' then 'Others' end end end end end end end as 'Sector_Activity'

  , dbo.OTJ_GetNBTAccount(
		PreparedData.CUAccountID,
		@dateTo,
		PreparedData.[Late Days],
		PreparedData.RSCHD1,
		PreparedData.[Product Activity],
		PreparedData.CustomerTypeID
	) AS NBT_Account

FROM(
	SELECT  CULoan.CustomerID as 'CustomerID',
					CULoan.CUAccountID as 'CUAccountID',
			CULoan.CULoanID as 'CULoanID',
			CUAccount.AccountNumber as 'Contract Code',
			Customer.Name as 'ClientName',
				Customer.CustomerType AS CustomerTypeID,

									case when MiscellaneousLists.DisplayMember='Personal' then 
				CASE Person.Gender  WHEN 0 THEN 'Male' WHEN 1 THEN 'Female' ELSE '-' end else '-' end AS 'Gender',

			[dbo].[_CustomerAgeAtDate](Customer.CustomerID,GETDATE()) as 'Age',
			Person.SocialSecurityNumber as 'Passport',
			Person.DrivingLicenceNumber as INN,
			concat(Person.Telephone1,' ',Person.Telephone2,' ',Person.Telephone3) as 'TelephoneNumber',
			CUAccountPortfolio.[Description] as 'Loan Officer', 
			MiscellaneousLists.DisplayMember 'CustomerType',
																case when  customer.CustomerType=8 then 
				(SELECT COUNT(l.CULoanID) FROM CULoan l wHERE l.CommunityCULoanID=CULoan.CULoanID) 
			else 1 end 'GroupCount',
			OTJ_Branches.Name as 'BranchName',
			OTJ_Branches.RegionalBranch as 'RegionalBranch',
			OTJ_Branches.Branch as 'Branch',
			OTJ_Branches.SubBranch as 'SubBranch',
			OTJ_Branches.OTJ_BranchID as 'OTJ_BranchID',
			dbo.[Address].County as 'District',
			[Address].TownCity+' '+[Address].Address1 as 'Client address',
			AddressListValue.Code as RuralUrban,
			CULoanPart.IssueDate as 'Start Date',

			CULoanPart.InitialPaymentDate as 'First ins date',
			CULoan.FinalPartDate as 'Close date',
			Currency.[Code] as 'Currency',
			Currency.CurrencyID as 'CurrencyID',
			dbo._GetCurrencyExchangeRate(1,CULoanPart.IssueDate) as 'Exchange Rate',
					CULoanPart.IssueAmount * [dbo].OTJ_GetXR(Currency.CurrencyID, 1, CULoanPart.IssueDate) as 'DisbursedInUSD',
					CULoanPart.IssueAmount * [dbo].OTJ_GetXR(Currency.CurrencyID, 18, CULoanPart.IssueDate) as 'DisbursedInTJS',
			[dbo].[OTJ_GetLoanCycle](CUAccount.CUAccountID, CUAccount.CustomerID) as 'Cycle',
				CUProduct.[Description] as 'Product',
			[dbo].[OTJ_GetInterestRate] (Cuaccount.CUAccountID) as 'InterestRate',
					[dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, @dateTo) AS 'Late Days',

				CULoanPart.PeriodsDeferred as 'Grace Period',
			CULoanPart.TermPeriodNum as 'Installment',
					CULoanPart.IssueFee1Percentage as 'IssueFee',
			case when CULoan.Restructured=1 then 'YES' else 'NO' end as 'RSCHD',
			CULoan.Restructured as 'RSCHD1',
			CUloan.LastRestructuredDate as 'RSCHD date',
					[dbo].[_AmountSizeClass](CULoanPart.IssueAmount * [dbo].OTJ_GetXR(Currency.CurrencyID, 1, CULoanPart.IssueDate),1) AS 'Loan size',
			[dbo].[_AmountSizeClassOperationDep](CULoanPart.IssueAmount * [dbo].OTJ_GetXR(Currency.CurrencyID, 18, CULoanPart.IssueDate),18) AS 'Loan size Oper TJS',
			ISNULL(GuarCount.GCount,0)as 'NumberOfGuarantors',
			CASE WHEN EXISTS (SELECT * FROM   CULoanCollateral WHERE CULoanCollateral.CULoanID = CULoan.CULoanID) THEN 'Yes' ELSE 'No' END AS Collaterals,
			CUProductLoanReasons.[Description] as 'LoanReason',
					ca11.[Description] as  'Client Activity1',
				ca22.[Description] as 'Client Activity2',
				AnalysisField.Name as 'Product Activity',
			CUAccountIndustryCode.[Description]  as 'Industry Code',
			[dbo].[OTJ_GetSubProduct](CUAccount.CUAccountID) AS 'Sub Product',
			(select CASE CHARINDEX(' ', [Description], 1) WHEN 0 THEN [Description] ELSE SUBSTRING([Description], 1, CHARINDEX(' ', [Description], 1) - 1) END
			from CUAccountIndustryCode where  CUAccount.CUAccountIndustryCodeID=CUAccountIndustryCode.CUAccountIndustryCodeID)  as 'Sector',
			ufl4041.[Description] 'MethodofAnalysis',
			job.Value as new_job

	FROM CULoan
	INNER JOIN Customer ON Customer.CustomerID = CULoan.CustomerID
	left JOIN CustomerPerson ON CustomerPerson.CustomerID = Customer.CustomerID 
	left JOIN Person ON CustomerPerson.PersonID = Person.PersonID
	INNER JOIN MiscellaneousLists ON Customer.CustomerType=MiscellaneousLists.ValueMember and  
																	MiscellaneousLists.Code like '%customertype%' and MiscellaneousLists.LanguageID=1
	INNER JOIN CUAccount ON CUAccount.CUAccountID = CULoan.CUAccountID
	LEFT JOIN CUAccountIndustryCode ON CUAccount.CUAccountIndustryCodeID=CUAccountIndustryCode.CUAccountIndustryCodeID
	Inner JOIN CULoanPart ON CULoanPart.CULoanID = CULoan.CULoanID and CULoanPart.Issued=1
	--added by FH 2019-02-11 for exclude reschedule loans
	INNER JOIN CUTransaction tr ON tr.ReceiptNo=CULoanPart.IssueReceiptNo AND (CONVERT(date, tr.ValueDate) BETWEEN @dateFrom AND @dateTo)
		AND tr.ReversalReceiptNo=0 AND tr.TransactionSourceID=1 AND tr.TransactionTypeID=8 AND tr.Amount>0

	INNER JOIN OTJ_Branches ON CUAccount.BranchID=OTJ_Branches.OTJ_BranchID
	LEFT JOIN (select  culoanid, count(culoanid) as 'GCount' from CULoanGuarantor group by CULoanID) GuarCount ON culoan.CULoanID=GuarCount.CULoanID
	LEFT JOIN CUProduct ON CULoan.ProductID=CUProduct.ProductID
	LEFT JOIN CUProductLoan ON CULoan.ProductID=CUProductLoan.ProductID
	LEFT JOIN CUAccountPortfolio ON CUAccount.CUAccountPortfolioID=CUAccountPortfolio.CUAccountPortfolioID
	INNER JOIN Currency ON CUProduct.CurrencyID=Currency.CurrencyID
	LEFT JOIN CustomerAddress ON Customer.CustomerID=CustomerAddress.CustomerID and CustomerAddress.AddressTypeID=1
	LEFT JOIN dbo.[Address] ON dbo.[Address].AddressID=CustomerAddress.AddressID
	LEFT JOIN AddressListValue ON AddressListValueID=dbo.[Address].CountyID
	LEFT JOIN CUProductLoanReasons ON CULoan.LoanReasonID= CUProductLoanReasons.LoanReasonID
	LEFT JOIN CUFee ON CUProductLoan.IssueFeeID=CUFee.CUFeeID
	LEFT JOIN CUFeeBand ON CUFee.CUFeeID=CUFeeBand.CUFeeID
	LEFT JOIN UserDefinedFieldLinks ca1 ON ca1.CustomerID=Customer.CustomerID and ca1.UserDefinedFieldID in (1)            
	LEFT JOIN UserDefinedFieldListValues ca11 ON  ca11.UserDefinedFieldListValueID=ca1.Value 
	LEFT JOIN UserDefinedFieldLinks ca2 ON ca2.CustomerID=Customer.CustomerID and ca2.UserDefinedFieldID in (2)            
	LEFT JOIN UserDefinedFieldListValues ca22 ON  ca22.UserDefinedFieldListValueID=ca2.Value
	LEFT JOIN UserDefinedFieldLinks job ON job.UserDefinedFieldID = 16 AND job.CUAccountID = CUAccount.CUAccountID
	LEFT JOIN AnalysisLink ON AnalysisLink.ProductID=CULoan.ProductID and AnalysisLink.AnalysisFieldID between 7 and 15
	LEFT JOIN AnalysisField ON AnalysisField.AnalysisFieldID=AnalysisLink.AnalysisFieldID and AnalysisField.AnalysisGroupID=2

		left join UserDefinedFieldLinks ufl404 on CUAccount.CUAccountID = ufl404.CUAccountID and ufl404.UserDefinedFieldID=404
		LEFT JOIN UserDefinedFieldListValues ufl4041 ON  ufl4041.UserDefinedFieldListValueID=ufl404.Value 

	where culoan.CommunityCULoanID is null
	) PreparedData

	where --dbo._CULoanStatusAtDate(PreparedData.CUAccountID,@dateTo) IN (4) and --commented by FH 2019-02-11 not need
	PreparedData.CurrencyID in (SELECT value FROM dbo.SplitString(@currencyFilter, ','))
	and PreparedData.OTJ_BranchID  in (SELECT value FROM dbo.SplitString(@branchFilter, ','))
	and cast(PreparedData.[Start Date] as date) between @dateFrom and @dateTo
)
GO
