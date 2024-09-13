
import json

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponse
import pypyodbc as odbc
from common.abacus.connection import connection_string

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def swift_search_client_extra(req):
  json_data = json.loads(req.body)

  conn = odbc.connect(connection_string)
  cursor = conn.cursor()
  cursor.execute(
    f"""SELECT
	c.Name,
	c.CustomerID AS client_ID,
	p.SocialSecurityNumber AS passport,
	p.DrivingLicenceNumber AS INN,
	b.Description AS branch_name,
	b.BranchID AS branch,
	a.AccountNumber AS credit_id,
	CONVERT(VARCHAR(10), p.DateOfBirth, 120) AS birthday,
	p.Gender AS gender,
	addr1.TownCityID AS address,
	addr1.Address1 AS address_street,
	addr2.TownCityID AS registration_address,
	addr2.Address1 AS registration_address_street,
	p.Telephone1 AS phone1,
	p.Telephone2 AS phone2,
	p.Telephone3 AS phone3,
	CONCAT(udfl.Value, ' ', udfl2.Value) AS passport_details,
	prod.Description AS credit_product,
	FLOOR(dbo._GetIssueAmount_OTJ(a.CUAccountID) * [dbo].OTJ_GetXR(cur.CurrencyID, 18, dbo._GetDisbusmentDate_OTJ(a.CUAccountID))) AS disbursed_tjs,
	lp.TermPeriodNum AS installment,
	cur.Code AS currency,
	CAST([dbo].[OTJ_GetInterestRate](a.CUAccountID) * 100 AS INTEGER) AS Interest_rate,
	FLOOR(dbo._BalanceAtDate(a.CUAccountID, GETDATE()) * [dbo].OTJ_GetXR(cur.CurrencyID, 18, GETDATE())) AS olb_tjs,
	CONVERT(VARCHAR(10), dbo._GetDisbusmentDate_OTJ(a.CUAccountID), 120) AS start_date,
	CONVERT(VARCHAR(10), (SELECT MAX(ls2.RepaymentDate) FROM CULoanSchedule ls2 WHERE ls2.CULoanPartID=lp.CULoanPartID), 120) AS close_date,
	CONVERT(VARCHAR(10), aa.StartDate, 120) AS close_date_fact,
	(SELECT TOP 1 CAST(ls.TotalRepayment AS INT) FROM CULoanSchedule ls WHERE ls.LoanRepayment > 0 AND ls.CULoanPartID = lp.CULoanPartID) AS total_repayment,

	(SELECT SUM(late_days_count)
	FROM (
		SELECT 
			(select COUNT(CASE WHEN lschd.ArearDaysFor > 0 THEN 1 END) from [dbo].OTJ_getSchedule(CUAccount.CUAccountID) lschd where lschd.RepaymentDate > DATEADD(year, -1, GETDATE())) as late_days_count
		FROM CUAccount
		INNER JOIN CULoan ON CULoan.CUAccountID = CUAccount.CUAccountID
		INNER JOIN CULoanPart ON CULoanPart.CULoanID = CULoan.CULoanID AND CULoanPart.Issued = 1 AND CULoanPart.CurrentPart = 1
		WHERE CULoan.Status IN (4, 8, 16)
		AND CUAccount.ParentAccountID IS NULL
		AND CUAccount.AccountNumber NOT LIKE '%.%'
		AND CUAccount.CustomerID = c.CustomerID
	) late_counts) as late_days_count,

	(SELECT SUM(late_days_sum)
	FROM (
		SELECT 
			(select SUM(lschd.ArearDaysFor) from [dbo].OTJ_getSchedule(CUAccount.CUAccountID) lschd where lschd.RepaymentDate > DATEADD(year, -1, GETDATE())) as late_days_sum
		FROM CUAccount
		INNER JOIN CULoan ON CULoan.CUAccountID = CUAccount.CUAccountID
		INNER JOIN CULoanPart ON CULoanPart.CULoanID = CULoan.CULoanID AND CULoanPart.Issued = 1 AND CULoanPart.CurrentPart = 1
		WHERE CULoan.Status IN (4, 8, 16)
		AND CUAccount.ParentAccountID IS NULL
		AND CUAccount.AccountNumber NOT LIKE '%.%'
		AND CUAccount.CustomerID = c.CustomerID
	) late_counts) as late_days_sum,

	[dbo].[OTJ_GetLoanCycle](a.CUAccountID, a.CustomerID) as 'Cycle',
	FLOOR((SELECT SUM(DATEDIFF(MONTH, CULoan.ApproveDate, CULoan.FinalPartDate)) from CULoan
		INNER JOIN CUAccount ON CUAccount.CUAccountID = CULoan.CUAccountID
		INNER JOIN Customer ON Customer.CustomerID = CUAccount.CustomerID
		WHERE CULoan.Status IN (4, 8, 16, 32) AND Customer.CustomerID = c.CustomerID)) AS duration_credit_history,
	FLOOR((SELECT SUM(dbo._GetIssueAmount_OTJ(CUAccount.CUAccountID) * [dbo].OTJ_GetXR(Currency.CurrencyID, 18, dbo._GetDisbusmentDate_OTJ(CUAccount.CUAccountID)))
		from CULoan
		INNER JOIN CUAccount ON CUAccount.CUAccountID = CULoan.CUAccountID
		INNER JOIN Customer ON Customer.CustomerID = CUAccount.CustomerID
		LEFT JOIN CUProduct ON CULoan.ProductID=CUProduct.ProductID
		LEFT JOIN Currency ON CUProduct.CurrencyID = Currency.CurrencyID
		WHERE CULoan.Status IN (4, 8, 16, 32) AND dbo._BalanceAtDate(CUAccount.CUAccountID, GETDATE()) > 0 AND Customer.CustomerID = c.CustomerID)) as disbursed_all,
	FLOOR((SELECT SUM(dbo._BalanceAtDate(CUAccount.CUAccountID, GETDATE()) * [dbo].OTJ_GetXR(Currency.CurrencyID, 18, GETDATE()))
		from CULoan
		INNER JOIN CUAccount ON CUAccount.CUAccountID = CULoan.CUAccountID
		INNER JOIN Customer ON Customer.CustomerID = CUAccount.CustomerID
		LEFT JOIN CUProduct ON CULoan.ProductID=CUProduct.ProductID
		LEFT JOIN Currency ON CUProduct.CurrencyID = Currency.CurrencyID
		WHERE CULoan.Status IN (4, 8, 16, 32) AND Customer.CustomerID = c.CustomerID)) AS olb_all,
	CASE WHEN [dbo].[OTJ_GetLateDays](a.CUAccountID, GETDATE()) > 0 AND dbo._BalanceAtDate(a.CUAccountID, GETDATE()) > 0 THEN N'Да' ELSE N'Нет' END AS late_days,
	CASE WHEN l.Restructured = 1 THEN N'Да' ELSE N'Нет' END AS 'RSCHD',
	CASE WHEN CUAccountPortfolio.Description LIKE '%kol%' OR CUAccountPortfolio.Description LIKE '%law%' THEN N'Да' ELSE N'Нет' END AS in_collector,
	CASE WHEN (select COUNT(*) from CULoan
		INNER JOIN CULoanGuarantor ON CULoanGuarantor.CULoanID = CULoan.CULoanID
		LEFT JOIN Customer ON Customer.CustomerID = CULoanGuarantor.CustomerID
		WHERE CULoan.Status = 16 AND Customer.CustomerID = c.CustomerID) > 0 THEN N'Да' ELSE N'Нет' END AS written_off_guarantor,
	CASE WHEN (select COUNT(*) from CULoan
		INNER JOIN CULoanGuarantor ON CULoanGuarantor.CULoanID = CULoan.CULoanID
		LEFT JOIN Customer ON Customer.CustomerID = CULoanGuarantor.CustomerID
		LEFT JOIN CUAccount ON CUAccount.CUAccountID = CULoan.CUAccountID
		WHERE dbo._BalanceAtDate(CUAccount.CUAccountID, GETDATE()) > 0 AND Customer.CustomerID = c.CustomerID) > 0 THEN N'Да' ELSE N'Нет' END AS guarantor_active_credit,
	CASE WHEN ISNULL(udflD.Value, 0) = 0 THEN N'Нет' ELSE N'Да' END AS court_case,
	CASE WHEN prod.Description LIKE '%EXPRESS LOAN%' AND dbo._BalanceAtDate(a.CUAccountID, GETDATE()) > 0 THEN N'Да' ELSE N'Нет' END have_active_express

FROM Customer c
INNER JOIN CustomerPerson cp ON cp.CustomerID = c.CustomerID
INNER JOIN Person p ON p.PersonID = cp.PersonID
LEFT JOIN Branches b ON b.BranchId = c.BranchId
LEFT JOIN CUAccount a ON a.CustomerID = c.CustomerID
	AND a.CUAccountID = (
		SELECT MAX(az.CUAccountID)
		FROM CUAccount az
		LEFT JOIN CULoan lz ON lz.CUAccountID=az.CUAccountID
		WHERE az.CustomerID = a.CustomerID AND az.ParentAccountID IS NULL AND lz.Status IN (4, 8, 16))
	AND a.AccountNumber NOT LIKE '%.%'
LEFT JOIN CULoan l ON l.CUAccountID = a.CUAccountID
LEFT JOIN CULoanPart lp ON lp.CULoanID = l.CULoanID AND lp.Issued = 1 AND lp.CurrentPart = 1
LEFT JOIN CUProduct prod ON l.ProductID=prod.ProductID
LEFT JOIN Currency cur ON prod.CurrencyID = cur.CurrencyID
LEFT JOIN CustomerAddress ca1 ON ca1.CustomerID = c.CustomerID AND ca1.AddressTypeID = 1
LEFT JOIN Address addr1 ON addr1.AddressID = ca1.AddressID
LEFT JOIN CustomerAddress ca2 ON ca2.CustomerID = c.CustomerID AND ca2.AddressTypeID = 2
LEFT JOIN Address addr2 ON addr2.AddressID = ca2.AddressID
LEFT JOIN UserDefinedFieldLinks udfl ON udfl.CustomerID = c.CustomerID AND udfl.UserDefinedFieldID = 3
LEFT JOIN UserDefinedFieldLinks udfl2 ON udfl2.CustomerID = c.CustomerID AND udfl2.UserDefinedFieldID = 4
LEFT JOIN CUAccountActive aa ON aa.CUAccountID = a.CUAccountID AND aa.Active = 0
LEFT JOIN CUAccountPortfolio ON CUAccountPortfolio.CUAccountPortfolioID = a.CUAccountPortfolioID
LEFT JOIN UserDefinedFieldLinks udflD ON udflD.CUAccountID=a.CUAccountID  AND udflD.UserDefinedFieldID=406
WHERE c.CustomerID = {json_data['client_ID']}"""
  )
  results = []
  columns = [column[0] for column in cursor.description]
  while True:
    row = cursor.fetchone()
    if not row:
        break
    result_dict = {column: row[column] for column in columns}
    results.append(result_dict)

  cursor.close()
  conn.close()
  return HttpResponse(status=HTTP_200_OK, content=json.dumps(results), content_type="application/json")