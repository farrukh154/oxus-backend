IF OBJECT_ID('abacus_active_loan') IS NOT NULL
    DROP FUNCTION abacus_active_loan
GO

CREATE FUNCTION abacus_active_loan
(	
	@dateFilter datetime,
	@currencyFilter char(300),
	@branchFilter char(300)
)
RETURNS TABLE 
AS
RETURN 
(
SELECT * FROM (
	SELECT  CULoan.CustomerID as 'CustomerID',
					CULoan.CUAccountID as 'CUAccountID',
			CULoan.CULoanID as 'CULoanID',
			CUAccount.AccountNumber as 'Contract Code',
			--ufl.Value,
			Customer.Name as 'ClientName',
			CUAccountPortfolio.[Description] as 'Loan Officer', 
			culoan.CommunityCULoanID,
			Customer.CustomerType as 'CustomerTypeID',
			MiscellaneousLists.DisplayMember 'CustomerType',
		
																	case when  customer.CustomerType=8 then 
				(SELECT COUNT(l.CULoanID) FROM CULoan l wHERE l.CommunityCULoanID=CULoan.CULoanID) 
			else 1 end 'GroupCount',

			dbo._GetDisbusmentDate_OTJ(CULoan.CUAccountID) as 'Start Date',
			CULoanPart.InitialPaymentDate as 'First ins date',
			CULoanPart.IssueAmount as 'Disbursed',
			dbo._BalanceAtDate(CUAccount.CUAccountID, @dateFilter)* [dbo].OTJ_GetXR(Currency.CurrencyID, 1, @dateFilter) as 'OLB USD',
																	dbo._BalanceAtDate(CUAccount.CUAccountID, @dateFilter) * [dbo].OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) as 'OLB TJS',
					dbo._InterestCalculator(CULoan.CUAccountID, @dateFilter, 1) AS 'Interest',
				CUProduct.[Description] as 'Product',
			[dbo].[OTJ_GetInterestRate] (Cuaccount.CUAccountID) as 'InterestRate',
			CULoanPart.TermPeriodNum as 'Installment',
			Currency.CurrencyID as 'CurrencyID',
			Currency.[Code] as 'Currency',
			OTJ_Branches.Name as 'BranchName',
			OTJ_Branches.RegionalBranch as 'RegionalBranch',
			OTJ_Branches.Branch as 'Branch',
			OTJ_Branches.SubBranch as 'Sub Branch',
			OTJ_Branches.OTJ_BranchID as 'OTJ_BranchID',
				[dbo].[_LateDaysBand](
						case when CUProductLoan.InterestMethod <> 8 then 
								case when  dbo._PrincipleArrearDays(CULoan.CUAccountID,@dateFilter) >=dbo._InterestArrearDays(CULoan.CUAccountID,@dateFilter) 
									then dbo._PrincipleArrearDays(CULoan.CUAccountID,@dateFilter) Else dbo._InterestArrearDays(CULoan.CUAccountID,@dateFilter) End
				Else  dbo._ArrearsDaysCapLoans(CULoanPart.CuLoanPartID,CUAccount.CUAccountID,@dateFilter, culoan.[status], CUAccount.active)  End ) AS 'Category PAR',

			CUProductLoanReasons.[Description] as 'LoanReason',
				[dbo].[_AmountSizeClass](CULoanPart.IssueAmount * [dbo].OTJ_GetXR(Currency.CurrencyID, 1, CULoanPart.IssueDate),1) AS 'Loan size from Dis',
		
					[dbo].[_AmountSizeClass](dbo._BalanceAtDate(CUAccount.CUAccountID, @dateFilter) * [dbo].OTJ_GetXR(Currency.CurrencyID, 1, @dateFilter),1) AS 'Loan size from OLB',
					ca11.[Description] as  'Client Activity1',
				ca22.[Description] as 'Client Activity2',
				AnalysisField.Name as 'Product Activity',
			(select [description] from CUAccountIndustryCode where  CUAccount.CUAccountIndustryCodeID=CUAccountIndustryCode.CUAccountIndustryCodeID)  as 'Industry Code'

	FROM CULoan     
		INNER JOIN Customer ON Customer.CustomerID = CULoan.CustomerID
		LEFT JOIN  (select CommunityID, count(*) as 'GroupMembersCount' from CustomerCommunity group by CommunityID) #tmpGroupCount 
																																			ON Customer.CustomerID=#tmpGroupCount.CommunityID
		INNER JOIN MiscellaneousLists ON Customer.CustomerType=MiscellaneousLists.ValueMember and  
																		MiscellaneousLists.Code like '%customertype%' and MiscellaneousLists.LanguageID=20
		INNER JOIN CUAccount ON CUAccount.CUAccountID = CULoan.CUAccountID  and dbo._CUAccountActiveAtDate(CUAccount.CUAccountID,@dateFilter)=1
		INNER JOIN OTJ_Branches ON CUAccount.BranchID=OTJ_Branches.OTJ_BranchID
		INNER JOIN CULoanPart ON CULoanPart.CULoanID = CULoan.CULoanID and  CULoanPart.Issued=1  and  dbo.OTJCurrentLoanPartAtDate(CUAccount.CUAccountID, CULoan.CULoanID, @dateFilter)<>-1
		LEFT JOIN CUProduct ON CULoan.ProductID=CUProduct.ProductID
		LEFT JOIN CUProductLoan ON CULoan.ProductID=CUProductLoan.ProductID
		LEFT JOIN CUAccountPortfolio ON CUAccount.CUAccountPortfolioID=CUAccountPortfolio.CUAccountPortfolioID
		INNER JOIN Currency ON CUProduct.CurrencyID=Currency.CurrencyID 
		LEFT JOIN CUProductLoanReasons ON CULoan.LoanReasonID= CUProductLoanReasons.LoanReasonID
		LEFT JOIN CUFee ON CUProductLoan.IssueFeeID=CUFee.CUFeeID
		LEFT JOIN UserDefinedFieldLinks  ca1 ON ca1.CustomerID=Customer.CustomerID and  ca1.UserDefinedFieldID in (1)            
		LEFT JOIN UserDefinedFieldListValues ca11 ON  ca11.UserDefinedFieldListValueID=ca1.Value 
		LEFT JOIN UserDefinedFieldLinks  ca2 ON ca2.CustomerID=Customer.CustomerID and  ca2.UserDefinedFieldID in (2)            
		LEFT JOIN UserDefinedFieldListValues ca22 ON  ca22.UserDefinedFieldListValueID=ca2.Value 
		LEFT JOIN AnalysisLink ON AnalysisLink.ProductID=CULoan.ProductID and AnalysisLink.AnalysisFieldID between 7 and 14
		LEFT JOIN AnalysisField ON AnalysisField.AnalysisFieldID=AnalysisLink.AnalysisFieldID and AnalysisField.AnalysisGroupID=2
		WHERE CULoan.CommunityCULoanID is null
	--  left join UserDefinedFieldLinks ufl on CUAccount.CUAccountID = ufl.CUAccountID


	--  where  ufl.UserDefinedFieldID = 89
	--and CUAccount.AccountNumber='016/040058988/BC_STD_TJS'
	) PreparedData

	where  dbo._CULoanStatusAtDate(PreparedData.CUAccountID,@dateFilter) IN (4)
	and PreparedData.CurrencyID in (SELECT value FROM dbo.SplitString(@currencyFilter, ','))
	and PreparedData.OTJ_BranchID  in (SELECT value FROM dbo.SplitString(@branchFilter, ','))
	and cast(PreparedData.[Start Date] as date) <=@dateFilter
)
GO
