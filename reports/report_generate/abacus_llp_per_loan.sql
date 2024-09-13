IF OBJECT_ID('abacus_llp_per_loan') IS NOT NULL
    DROP FUNCTION abacus_llp_per_loan
GO

CREATE FUNCTION abacus_llp_per_loan
(	
	@dateFilter datetime,
	@currencyFilter char(300),
	@branchFilter char(300)
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT * ,
 case when PreparedData.Sector=N'Савдо' then 'Trade'
   else case when PreparedData.Sector=N'Растанипарварӣ' then 'Horticulture'
   else case when PreparedData.Sector=N'Истеҳсолот' then 'Production'
   else case when PreparedData.Sector=N'Истеъмолот' then 'Consumer'
   else case when PreparedData.Sector=N'Чорвопарварӣ' then 'Livestock'
   else case when PreparedData.Sector=N'Хизматрасонӣ' then 'Service'
   else case when PreparedData.Sector=N'Ғайраҳо' then 'Others' end end end end end end end as 'Sector_Activity',

   dbo.OTJ_GetNBTAccount(
		PreparedData.CUAccountID,
		@dateFilter,
		PreparedData.[Late_Days0],
		PreparedData.RSCHD,
		PreparedData.[Product Activity],
		PreparedData.CustomerTypeID
	) AS NBT_Account


FROM (
SELECT  CULoan.CustomerID as 'CustomerID',
        CULoan.CUAccountID as 'CUAccountID',
		CULoan.CULoanID as 'CULoanID',
		CUAccount.AccountNumber as 'Contract Code',
		Customer.Name as 'ClientName',
		Customer.CustomerType AS CustomerTypeID,
		CUAccountPortfolio.[Description] as 'Loan Officer', 
		MiscellaneousLists.DisplayMember 'CustomerType',

	    case when  customer.CustomerType=8 then 
		  (SELECT COUNT(l.CULoanID) FROM CULoan l wHERE l.CommunityCULoanID=CULoan.CULoanID) 
		else 1 end 'GroupCount',

		dbo._GetDisbusmentDate_OTJ(CULoan.CUAccountID) as 'Start Date',
		CULoanPart.InitialPaymentDate as 'First ins date', -- not correct if rescheduled
        (SELECT MAX(ls2.RepaymentDate) FROM CULoanSchedule ls2 WHERE ls2.CULoanPartID=CULoanPart.CULoanPartID) AS 'Close date',

		Currency.CurrencyID as 'CurrencyID',
		case when Currency.CurrencyID=18 then 'TJS' else 'USD' end as 'Currency',
		dbo._GetCurrencyExchangeRate(1, dbo._GetDisbusmentDate_OTJ(CULoan.CUAccountID)) as 'Exchange Rate',
        dbo._GetIssueAmount_OTJ(CULoan.CUAccountID) * [dbo].OTJ_GetXR(Currency.CurrencyID, 1, dbo._GetDisbusmentDate_OTJ(CULoan.CUAccountID)) as 'DisbursedInUSD',
        dbo._GetIssueAmount_OTJ(CULoan.CUAccountID) * [dbo].OTJ_GetXR(Currency.CurrencyID, 18, dbo._GetDisbusmentDate_OTJ(CULoan.CUAccountID)) as 'DisbursedInTJS',

		dbo._BalanceAtDate(CUAccount.CUAccountID, @dateFilter)* [dbo].OTJ_GetXR(Currency.CurrencyID, 1, @dateFilter) as 'OLBInUSD',
		dbo._BalanceAtDate(CUAccount.CUAccountID, @dateFilter) * [dbo].OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) as 'OLBInTJS',

		[dbo].[OTJ_GetInterestRate] (Cuaccount.CUAccountID) as 'InterestRate',
		dbo._InterestCalculator(CULoan.CUAccountID, @dateFilter, 1) AS 'Interest',
		CUProduct.[Description] as 'Product',

	 --   CULoanPart.PeriodsDeferred as 'Initial_GracePeriod',
		--CULoanPart.TermPeriodNum as 'Total_Installment',
	 --   case when CULoan.Restructured=1
		--	then 
		--		dbo._GetInitialTermPeriod_OTJ(CUAccount.CUAccountID) 
  --          else CULoanPart.TermPeriodNum
		--end as 'Initial_Installment',
		--datediff(M,CUloan.LastRestructuredDate, CULoan.FinalPartDate) as 'Installment_RSCHD',
	 --   dbo._GetInitialGracePeriod_OTJ(CUAccount.CUAccountID) as 'GracePeriod_RSCHD',

		case when CULoan.Restructured=1 THEN
			dbo._GetInitialTermPeriod_OTJ(CUAccount.CUAccountID)
		ELSE CULoanPart.TermPeriodNum END AS Installment_initial,
		case when CULoan.Restructured=1 THEN
			dbo._GetInitialGracePeriod_OTJ(CUAccount.CUAccountID)
		ELSE CULoanPart.PeriodsDeferred END AS GracePeriod_initial,

		case when CULoan.Restructured=1 then	
			CULoanPart.TermPeriodNum
		ELSE 0 END AS Installment_RSCHD,
		case when CULoan.Restructured=1 then
		(
			SELECT count(ls.Period) FROM CULoanSchedule ls WHERE ls.LoanRepayment = 0
			AND ls.CULoanPartID = CULoanPart.CULoanPartID
		) ELSE 0 END AS GracePeriod_RSCHD,
		case when CULoan.Restructured=1 then
		(
			SELECT count(ls.Period) FROM CULoanSchedule ls WHERE ls.LoanRepayment = 0 AND ls.InterestRepayment = 0
			AND ls.CULoanPartID = CULoanPart.CULoanPartID
		) ELSE 0 END AS GracePeriodInterest_RSCHD,


		CULoanPart.IssueFee1Percentage as 'IssueFee', -- not correct if rescheduled
		CUProductLoan.PenaltyInterestRate as 'PenaltyInterestRate',

		OTJ_Branches.Name as 'BranchName',
		OTJ_Branches.Branch as 'Branch',
		OTJ_Branches.SubBranch as 'SubBranch',
		OTJ_Branches.OTJ_BranchID as 'OTJ_BranchID',
		dbo.[Address].County as 'District',
		AddressListValue.Code as RuralUrban,
	    --case when dbo._ArrearsDays(CULoanPart.CuLoanPartID,CUAccount.CUAccountID,@dateFilter, 4, 1) >=dbo._InterestArrearDays(CULoan.CUAccountID,@dateFilter) 
     --       then dbo._ArrearsDays(CULoanPart.CuLoanPartID,CUAccount.CUAccountID,@dateFilter, 4, 1) Else dbo._InterestArrearDays(CULoan.CUAccountID,@dateFilter) End AS 'Late Days',
		[dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, @dateFilter) AS 'Late_Days0',
		[dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, EOMONTH(DATEADD(MONTH,-1,@dateFilter))) AS 'Late_Days1',
		[dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, EOMONTH(DATEADD(MONTH,-2,@dateFilter))) AS 'Late_Days2',
		[dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, EOMONTH(DATEADD(MONTH,-3,@dateFilter))) AS 'Late_Days3',
		[dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, EOMONTH(DATEADD(MONTH,-4,@dateFilter))) AS 'Late_Days4',
		[dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, EOMONTH(DATEADD(MONTH,-5,@dateFilter))) AS 'Late_Days5',
		[dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, EOMONTH(DATEADD(MONTH,-6,@dateFilter))) AS 'Late_Days6',
        [dbo].[_LateDaysBand]([dbo].[OTJ_GetLateDays](CUAccount.CUAccountID, @dateFilter)) AS 'Category PAR',
		CULoan.Restructured as 'RSCHD',
		CUloan.LastRestructuredDate as 'RSCHD date',
		(select count(l2.CULoanID)-1 from CUAccount a2 left join CULoan l2 on a2.CUAccountID=l2.CUAccountID
		where a2.CUAccountID=CUAccount.CUAccountID AND l2.Status not in (64) and l2.Status > 2) as 'RSCHD Count',
		udflD.Value as 'DateOfCourtCases',
		CUProductLoanReasons.[Description] as 'LoanReason',
        [dbo].[_AmountSizeClass](dbo._GetIssueAmount_OTJ(CULoan.CUAccountID) * [dbo].OTJ_GetXR(Currency.CurrencyID, 1, dbo._GetDisbusmentDate_OTJ(CULoan.CUAccountID)),1) AS 'Loan size from Dis',
        [dbo].[_AmountSizeClass](dbo._BalanceAtDate(CUAccount.CUAccountID, @dateFilter)* [dbo].OTJ_GetXR(Currency.CurrencyID, 1, @dateFilter),1) AS 'Loan size from OLB',

  	    ca11.[Description] as  'Client Activity1',
	    ca22.[Description] as 'Client Activity2',
	    AnalysisField.Name as 'Product Activity',
		[dbo].[OTJ_GetLoanCycle](CUAccount.CUAccountID, CUAccount.CustomerID) as 'Cycle',
		CUAccountIndustryCode.[Description] as 'Industry Code',
				(select CASE CHARINDEX(' ', [Description], 1) WHEN 0 THEN [Description] ELSE SUBSTRING([Description], 1, CHARINDEX(' ', [Description], 1) - 1) END
		 from CUAccountIndustryCode where  CUAccount.CUAccountIndustryCodeID=CUAccountIndustryCode.CUAccountIndustryCodeID)  as 'Sector',
		[dbo].[OTJ_GetSubProduct](CUAccount.CUAccountID) AS 'Sub Product',

		ufl4041.[Description] 'MethodofAnalysis',

		(SELECT SUM(CULoanCollateral.GrossValue) * dbo.OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) FROM CULoanCollateral LEFT JOIN CULoanCollateralType ON CULoanCollateralType.CULoanCollateralTypeID = CULoanCollateral.CULoanCollateralTypeID
		WHERE CULoanCollateral.CULoanID=CULoan.CULoanID AND CULoanCollateralType.CULoanCollateralTypeID=1 AND CULoanCollateral.IsDeleted=0) AS Collateral_Vehicle,
		(SELECT SUM(CULoanCollateral.GrossValue) * dbo.OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) FROM CULoanCollateral LEFT JOIN CULoanCollateralType ON CULoanCollateralType.CULoanCollateralTypeID = CULoanCollateral.CULoanCollateralTypeID
		WHERE CULoanCollateral.CULoanID=CULoan.CULoanID AND CULoanCollateralType.CULoanCollateralTypeID=2 AND CULoanCollateral.IsDeleted=0) AS Collateral_Turnover,
		(SELECT SUM(CULoanCollateral.GrossValue) * dbo.OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) FROM CULoanCollateral LEFT JOIN CULoanCollateralType ON CULoanCollateralType.CULoanCollateralTypeID = CULoanCollateral.CULoanCollateralTypeID
		WHERE CULoanCollateral.CULoanID=CULoan.CULoanID AND CULoanCollateralType.CULoanCollateralTypeID=3 AND CULoanCollateral.IsDeleted=0) AS Collateral_Equipment,
		(SELECT SUM(CULoanCollateral.GrossValue) * dbo.OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) FROM CULoanCollateral LEFT JOIN CULoanCollateralType ON CULoanCollateralType.CULoanCollateralTypeID = CULoanCollateral.CULoanCollateralTypeID
		WHERE CULoanCollateral.CULoanID=CULoan.CULoanID AND CULoanCollateralType.CULoanCollateralTypeID=4 AND CULoanCollateral.IsDeleted=0) AS Collateral_HomeAssets,
		(SELECT SUM(CULoanCollateral.GrossValue) * dbo.OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) FROM CULoanCollateral LEFT JOIN CULoanCollateralType ON CULoanCollateralType.CULoanCollateralTypeID = CULoanCollateral.CULoanCollateralTypeID
		WHERE CULoanCollateral.CULoanID=CULoan.CULoanID AND CULoanCollateralType.CULoanCollateralTypeID=5 AND CULoanCollateral.IsDeleted=0) AS Collateral_FutureHarvest,
		(SELECT SUM(CULoanCollateral.GrossValue) * dbo.OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) FROM CULoanCollateral LEFT JOIN CULoanCollateralType ON CULoanCollateralType.CULoanCollateralTypeID = CULoanCollateral.CULoanCollateralTypeID
		WHERE CULoanCollateral.CULoanID=CULoan.CULoanID AND CULoanCollateralType.CULoanCollateralTypeID=6 AND CULoanCollateral.IsDeleted=0) AS Collateral_RealEstate,
		(SELECT SUM(CULoanCollateral.GrossValue) * dbo.OTJ_GetXR(Currency.CurrencyID, 18, @dateFilter) FROM CULoanCollateral LEFT JOIN CULoanCollateralType ON CULoanCollateralType.CULoanCollateralTypeID = CULoanCollateral.CULoanCollateralTypeID
		WHERE CULoanCollateral.CULoanID=CULoan.CULoanID AND CULoanCollateralType.CULoanCollateralTypeID=7 AND CULoanCollateral.IsDeleted=0) AS Collateral_Gold,

		(SELECT COUNT(CULoanGuarantor.CULoanGuarantorID) FROM CULoanGuarantor
		WHERE CULoanGuarantor.CULoanID=CULoan.CULoanID AND CULoanGuarantor.Active = 1) AS Guarantor,

		case when  culoan.CULoanRefinanceReasonID=1 then 'YES' else 'NO' end as 'COVID19Restructures'
		
FROM CULoan     
INNER JOIN Customer ON Customer.CustomerID = CULoan.CustomerID
INNER JOIN MiscellaneousLists ON Customer.CustomerType=MiscellaneousLists.ValueMember and  
                                MiscellaneousLists.Code like '%customertype%' and MiscellaneousLists.LanguageID=1
INNER JOIN CUAccount ON CUAccount.CUAccountID = CULoan.CUAccountID and dbo._CUAccountActiveAtDate(CUAccount.CUAccountID,@dateFilter)=1
LEFT JOIN CUAccountIndustryCode ON CUAccount.CUAccountIndustryCodeID=CUAccountIndustryCode.CUAccountIndustryCodeID
INNER JOIN OTJ_Branches ON CUAccount.BranchID=OTJ_Branches.OTJ_BranchID  
INNER JOIN CULoanPart ON CULoanPart.CULoanID = CULoan.CULoanID and CULoanPart.Issued=1 and dbo.OTJCurrentLoanPartAtDate(CUAccount.CUAccountID, CULoan.CULoanID, @dateFilter)<>-1
JOIN CUProduct ON CULoan.ProductID=CUProduct.ProductID
LEFT JOIN CUProductLoan ON CULoan.ProductID=CUProductLoan.ProductID
LEFT JOIN CUAccountPortfolio ON CUAccount.CUAccountPortfolioID=CUAccountPortfolio.CUAccountPortfolioID
INNER JOIN Currency ON CUProduct.CurrencyID=Currency.CurrencyID 
LEFT JOIN CustomerAddress ON Customer.CustomerID=CustomerAddress.CustomerID and CustomerAddress.AddressTypeID=1
LEFT JOIN dbo.[Address] ON dbo.[Address].AddressID=CustomerAddress.AddressID
LEFT JOIN AddressListValue ON AddressListValueID=dbo.[Address].CountyID
LEFT JOIN CUProductLoanReasons ON CULoan.LoanReasonID= CUProductLoanReasons.LoanReasonID
LEFT JOIN CUFee ON CUProductLoan.IssueFeeID=CUFee.CUFeeID
LEFT JOIN CUFeeBand ON CUFee.CUFeeID=CUFeeBand.CUFeeID
LEFT JOIN UserDefinedFieldLinks  ca1 ON ca1.CustomerID=Customer.CustomerID and  ca1.UserDefinedFieldID in (1)            
LEFT JOIN UserDefinedFieldListValues ca11 ON  ca11.UserDefinedFieldListValueID=ca1.Value 
LEFT JOIN UserDefinedFieldLinks  ca2 ON ca2.CustomerID=Customer.CustomerID and  ca2.UserDefinedFieldID in (2)            
LEFT JOIN UserDefinedFieldListValues ca22 ON  ca22.UserDefinedFieldListValueID=ca2.Value 
LEFT JOIN AnalysisLink ON AnalysisLink.ProductID=CULoan.ProductID and AnalysisLink.AnalysisFieldID between 7 and 15
LEFT JOIN AnalysisField ON AnalysisField.AnalysisFieldID=AnalysisLink.AnalysisFieldID and AnalysisField.AnalysisGroupID=2

  left join UserDefinedFieldLinks ufl404 on CUAccount.CUAccountID = ufl404.CUAccountID and ufl404.UserDefinedFieldID=404
  LEFT JOIN UserDefinedFieldListValues ufl4041 ON  ufl4041.UserDefinedFieldListValueID=ufl404.Value 
   LEFT JOIN UserDefinedFieldLinks udflD ON udflD.CUAccountID=CUAccount.CUAccountID  AND udflD.UserDefinedFieldID=406

  where CULoan.CommunityCULoanID is null  
) PreparedData
where 
	dbo._CULoanStatusAtDate(PreparedData.CUAccountID,@dateFilter) IN (4) and 
	PreparedData.CurrencyID in (SELECT value FROM dbo.SplitString(@currencyFilter, ','))
	and PreparedData.OTJ_BranchID  in (SELECT value FROM dbo.SplitString(@branchFilter, ','))
	and cast(PreparedData.[Start Date] as date) <=@dateFilter
)
GO
