import pypyodbc as odbc
from django.http import JsonResponse
import json
from django.http import HttpResponse
from division.models.branch.model import Branch
from common.abacus.connection import connection_string
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_terminal_records(request):
    data = json.loads(request.body.decode("utf-8")) if request.body else {}
    date_from = data.get("dateFrom", None )
    date_to = data.get("dateTo", None)
    branches = data.get("branch", '')
    display_currency = data.get("displayCurrency", None)
    conversion_currency = data.get("conversionCurrency", 18)

    afClientCode = data.get("afClientCode", None)
    afCreditCode = data.get("afCreditCode", None)
    afDateFrom = data.get("afDateFrom", None)
    afDateTo = data.get("afDateTo", None)


    branch_ids = [
        int(branch_id) for branch_id in branches.split(",") if branch_id.isdigit()
    ]

    branch_objects = Branch.objects.filter(id__in=branch_ids)

    branch_abacus_ids = [branch.abacus_id for branch in branch_objects]
    branch_abacus_ids_str = ','.join(str(x) for x in branch_abacus_ids)

    conn = odbc.connect(connection_string)
    cursor = conn.cursor()

    if afClientCode or afCreditCode:
        if afClientCode:
            filter = f"""c.CustomerID={afClientCode}"""
        if afCreditCode:
            filter = f"""a.AccountNumber like N'%{afCreditCode}%'"""
        if afDateFrom and afDateTo:
            filter += f"""AND cast(tp.PayDate as date) between '{afDateFrom}' and '{afDateTo}'"""
    else:
        filter = f"""(({display_currency} = 0) OR (cur.CurrencyID= {display_currency}))
        AND br.OTJ_BranchID in ({branch_abacus_ids_str})
        AND cast(tp.PayDate as date) between '{date_from}' and '{date_to}'"""

    cursor.execute(
    f"""SELECT TOP 100
    tp.id,
    CONVERT(VARCHAR(10), tp.PayDate, 120) AS PayDate,
    ROUND(tp.Amount*[dbo].OTJ_GetXR(18, {conversion_currency}, tp.PayDate), 2) Amount,
    'Credit' TypeOper,
    c.Name,
    a.AccountNumber,
    'Payment from terminal '+tv.Name Notes,
    br.Branch,
    tp.AccountNumber AS tpAccountNumber,
    c.CustomerID,
    br.SubBranch,
    tp.TransactionID
    FROM OTJ_TerminalPay tp
    LEFT JOIN CUAccount a ON SUBSTRING(a.AccountNumber,5,9) = tp.AccountNumber AND a.ParentAccountID IS NULL
    LEFT JOIN OTJ_TerminalVendor tv ON tv.id=tp.VendorId
    LEFT JOIN Customer c ON c.CustomerID=a.CustomerID
    LEFT JOIN CULoan l ON l.CULoanID=(SELECT TOP(1) l2.CULoanID FROM CULoan l2 WHERE
    l2.[Status]<>64 AND l2.CUAccountID=a.CUAccountID ORDER BY l2.ApplyDate DESC)
    LEFT JOIN CULoanPart lp ON lp.CULoanID=l.CULoanID
    LEFT JOIN CUProduct p ON p.ProductID=l.ProductID
    LEFT JOIN CUProductLoan pl ON pl.ProductID=p.ProductID
    LEFT JOIN Currency cur ON cur.CurrencyID=p.CurrencyID
    INNER JOIN OTJ_Branches br ON a.BranchID=br.OTJ_BranchID
    WHERE
    {filter}
    AND l.CommunityCULoanID is null
    ORDER BY tp.id asc""",
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
