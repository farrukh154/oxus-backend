IF OBJECT_ID('abacus_swift_loan') IS NOT NULL
    DROP FUNCTION abacus_swift_loan
GO

CREATE FUNCTION abacus_swift_loan
(	
	@dateFilter datetime
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT
	MAX(Branch) AS Branch,
	MAX(SubBranch) AS SubBranch,
	MAX(Name) AS Name,
	MAX(gender) AS gender,
	MAX(age) AS age,
	CustomerID,
	MAX(Passport) AS Passport,
	MAX(INN) AS INN,
	MAX(phone) AS phone,
	MAX(phone2) AS phone2,
	MAX(phone3) AS phone3,
	(CASE WHEN dbo._BalanceAtDate(MAX(CUAccountIDD), @dateFilter) * [dbo].OTJ_GetXR((SELECT TOP 1 CUProduct.CurrencyID FROM CULoan LEFT JOIN CUProduct ON CUProduct.ProductID = CULoan.ProductID WHERE CULoan.CUAccountID = MAX(CUAccountIDD)), 18, @dateFilter) > 0
	THEN 'Active' ELSE 'Inactive' END) AS status,
	(
		dbo._GetIssueAmount_OTJ(MAX(CUAccountIDD)) *
		[dbo].OTJ_GetXR((SELECT TOP 1 CUProduct.CurrencyID FROM CULoan LEFT JOIN CUProduct ON CUProduct.ProductID = CULoan.ProductID WHERE CULoan.CUAccountID = MAX(CUAccountIDD)), 18, dbo._GetDisbusmentDate_OTJ(MAX(CUAccountIDD)))
	) AS DisbursedInTJS,
	MAX(currency) AS currency,
	[dbo].[OTJ_GetInterestRate](MAX(CUAccountIDD)) / 100 AS InterestRate,
	COUNT(cycle) AS cycle,
	([dbo]._BalanceAtDate(MAX(CUAccountIDD), @dateFilter) * [dbo].OTJ_GetXR((SELECT TOP 1 CUProduct.CurrencyID FROM CULoan LEFT JOIN CUProduct ON CUProduct.ProductID = CULoan.ProductID WHERE CULoan.CUAccountID = MAX(CUAccountIDD)), 18, @dateFilter)) as OLBInTJS,
	MAX(StartDate) AS StartDate,
	MAX(CloseDate) AS CloseDate,
	MAX(CloseDateFact) AS CloseDateFact,
	SUM(NumberDelinquency) AS NumberDelinquency,
	SUM(DayNumberDelinquency) AS DayNumberDelinquency,
	(
		SELECT TOP 1 AnalysisField.Name
		FROM CULoan
		LEFT JOIN AnalysisLink ON AnalysisLink.ProductID=CULoan.ProductID and AnalysisLink.AnalysisFieldID between 7 and 15
		LEFT JOIN AnalysisField ON AnalysisField.AnalysisFieldID=AnalysisLink.AnalysisFieldID and AnalysisField.AnalysisGroupID=2
		WHERE CULoan.CUAccountID = MAX(CUAccountIDD) and AnalysisLink.ProductID=CULoan.ProductID and AnalysisLink.AnalysisFieldID between 7 and 14
		ORDER BY CULoan.CULoanID DESC
	) AS ProductActivity,
	MAX(ClientActivity1) AS ClientActivity1,
	MAX(ClientActivity2) AS ClientActivity2,
	(
		SELECT TOP 1 CUProduct.[Description]
		FROM CULoan
		LEFT JOIN CUProduct ON CUProduct.ProductID = CULoan.ProductID
		WHERE CULoan.CUAccountID = MAX(CUAccountIDD)
	) AS Product,
	(
		SELECT CUAccountIndustryCode.[Description]
		FROM CUAccount
		LEFT JOIN CUAccountIndustryCode ON CUAccountIndustryCode.CUAccountIndustryCodeID = CUAccount.CUAccountIndustryCodeID
		WHERE CUAccount.CUAccountID = MAX(CUAccountIDD)
	) AS IndustryCode,
	(
		SELECT ufl4041.[Description]
		FROM CUAccount
		LEFT JOIN UserDefinedFieldLinks ufl404 ON CUAccount.CUAccountID = ufl404.CUAccountID and ufl404.UserDefinedFieldID=404
		LEFT JOIN UserDefinedFieldListValues ufl4041 ON ufl4041.UserDefinedFieldListValueID=ufl404.Value
		WHERE CUAccount.CUAccountID = MAX(CUAccountIDD)
	) AS MethodofAnalysis,
	MAX(LoanOfficerIfInCollector) AS LoanOfficerIfInCollector,
	MAX(Restructured) AS Restructured,
	MAX(late_days) AS late_days,
	MAX(DateOfCortCases) AS DateOfCortCases
FROM (
SELECT
ac.CUAccountID AS CUAccountIDD,
b.Branch,
b.SubBranch,
c.Name,
CASE WHEN p.Gender = 0 THEN 'Male' ELSE 'Female' END AS gender,
DATEDIFF(year, p.DateOfBirth, @dateFilter) AS age,
c.CustomerID,
p.SocialSecurityNumber AS Passport,
p.DrivingLicenceNumber AS INN,
p.Telephone1 AS phone,
p.Telephone2 AS phone2,
p.Telephone3 AS phone3,
cur.Code as currency,
1 AS cycle,
dbo._GetDisbusmentDate_OTJ(l.CUAccountID) as StartDate,
(SELECT MAX(ls2.RepaymentDate) FROM CULoanSchedule ls2 WHERE ls2.CULoanPartID=lp.CULoanPartID) AS CloseDate,
aa.StartDate AS CloseDateFact,

(select COUNT(CASE WHEN lschd.ArearDaysFor > 0 THEN 1 END) from [dbo].OTJ_getSchedule(l.CUAccountID) lschd where lschd.RepaymentDate > DATEADD(year, -1, @dateFilter)) AS NumberDelinquency,

(select SUM(lschd.ArearDaysFor) from [dbo].OTJ_getSchedule(l.CUAccountID) lschd where lschd.RepaymentDate > DATEADD(year, -1, @dateFilter)) AS DayNumberDelinquency,

ca11.[Description] as ClientActivity1,
ca22.[Description] as ClientActivity2,
CAST(l.Restructured AS tinyint) as Restructured,
CASE
	WHEN CHARINDEX('kol', CUAccountPortfolio.[Description]) > 0 THEN CUAccountPortfolio.[Description]
	WHEN CHARINDEX('law', CUAccountPortfolio.[Description]) > 0 THEN CUAccountPortfolio.[Description]
ELSE NULL END AS LoanOfficerIfInCollector,
CASE WHEN dbo._BalanceAtDate(l.CUAccountID, @dateFilter)> 0 THEN [dbo].[OTJ_GetLateDays](ac.CUAccountID, @dateFilter) ELSE 0 END AS late_days,
udflD.Value as DateOfCortCases,
ac.AccountNumber

FROM CULoan l
INNER JOIN CUAccount ac ON ac.CUAccountID = l.CUAccountID AND ac.ParentAccountID IS NULL
LEFT JOIN CUAccountActive aa ON aa.CUAccountID = ac.CUAccountID AND aa.Active = 0
INNER JOIN CULoanPart lp ON lp.CULoanID = l.CULoanID AND lp.Issued = 1 AND lp.CurrentPart = 1
JOIN CUProduct prod ON l.ProductID=prod.ProductID
INNER JOIN Currency cur ON prod.CurrencyID = cur.CurrencyID
INNER JOIN Customer c ON c.CustomerID = l.CustomerID
INNER JOIN CustomerPerson cp ON c.CustomerID = cp.CustomerID
INNER JOIN Person p ON p.PersonID = cp.PersonID
INNER JOIN OTJ_Branches b ON b.OTJ_BranchID = ac.BranchID
LEFT JOIN UserDefinedFieldLinks  ca1 ON ca1.CustomerID=c.CustomerID and  ca1.UserDefinedFieldID in (1)            
LEFT JOIN UserDefinedFieldListValues ca11 ON ca11.UserDefinedFieldListValueID=ca1.Value
LEFT JOIN UserDefinedFieldLinks  ca2 ON ca2.CustomerID=c.CustomerID and  ca2.UserDefinedFieldID in (2)            
LEFT JOIN UserDefinedFieldListValues ca22 ON ca22.UserDefinedFieldListValueID=ca2.Value
LEFT JOIN CUAccountPortfolio ON ac.CUAccountPortfolioID=CUAccountPortfolio.CUAccountPortfolioID
LEFT JOIN UserDefinedFieldLinks udflD ON udflD.CUAccountID=ac.CUAccountID AND udflD.UserDefinedFieldID=406

WHERE ac.AccountNumber NOT LIKE '%.%'
AND dbo._GetIssueAmount_OTJ(l.CUAccountID) > 0
AND l.Status IN (4, 8, 16)
--ORDER BY ac.CUAccountID DESC
) preparedData
GROUP BY preparedData.CustomerID
)
GO
