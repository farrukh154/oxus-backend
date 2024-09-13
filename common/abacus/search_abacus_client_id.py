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
def search_abacus_client_id(req):
  json_data = json.loads(req.body)
  client_id = json_data['clientId']
  conn = odbc.connect(connection_string)
  cursor = conn.cursor()
  cursor.execute(
    f"""
    SELECT
    c.CustomerID,
    c.Number,
    c.Name,
    CASE WHEN p.Gender = 0 THEN N'Муж' ELSE N'Жен' END gender,
    p.SocialSecurityNumber passport,
    p.DrivingLicenceNumber inn,
	CONVERT(VARCHAR(10), p.DateOfBirth, 120) DateOfBirth,
	b.Description clientbranch,
    a.CUAccountID,
	CONVERT(VARCHAR(10), l.ApplyDate, 120) ApplyDate,
    a.AccountNumber,
    lp.Issued,
    lp.CurrentPart,
    a.Active,
    CONVERT(VARCHAR(10), lp.IssueDate, 120) IssueDate,
	CAST(lp.IssueAmount AS VARCHAR) IssueAmount,
	CAST(a.DRAmount - a.CRAmount AS VARCHAR) olb,
	cb.Description creditbranch
FROM Customer c
LEFT JOIN CustomerPerson cp ON cp.CustomerID=c.CustomerID
LEFT JOIN Person p ON p.PersonID=cp.PersonID
LEFT JOIN CUAccount a ON a.CustomerID=c.CustomerID AND a.ParentAccountID IS NULL
LEFT JOIN CULoan l on l.CUAccountID=a.CUAccountID
LEFT JOIN CULoanPart lp on lp.CULoanID=l.CULoanID
LEFT JOIN Branches b ON b.BranchID=C.BranchID
LEFT JOIN Branches cb ON cb.BranchID=a.BranchID
WHERE c.CustomerID={client_id}
    """
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