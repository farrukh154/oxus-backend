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
def search_abacus_advanced(req):
  json_data = json.loads(req.body)
  search_filter = []
  if 'client_ID' in json_data:
    search_filter.append(f"c.CustomerID={json_data['client_ID']}")
  if 'credit_ID' in json_data:
    search_filter.append(f"a.AccountNumber LIKE N'%{json_data['credit_ID']}%'")
  if 'name' in json_data:
    search_filter.append(f"c.Name LIKE N'%{json_data['name']}%'")
  if 'passport' in json_data:
    search_filter.append(f"p.SocialSecurityNumber LIKE N'%{json_data['passport']}%'")
  if 'INN' in json_data:
    search_filter.append(f"p.DrivingLicenceNumber LIKE N'%{json_data['INN']}%'")

  search_filter_string = ' AND '.join(search_filter)
  print(search_filter_string)
  conn = odbc.connect(connection_string)
  cursor = conn.cursor()
  cursor.execute(
    f"""select TOP 100 a.CustomerID,
    a.AccountNumber,
    a.CUAccountID,
    lp.Issued,
    a.Active,
    l.Status,
    c.Name,
    p.SocialSecurityNumber AS passport,
    p.DrivingLicenceNumber AS INN,
    b.Description AS branch_name
    from CUAccount a
    left join CULoan l on l.CUAccountID=a.CUAccountID
    left join CULoanPart lp on lp.CULoanID=l.CULoanID
    left join Customer c ON c.CustomerID = a.CustomerID
    left JOIN CustomerPerson cp ON cp.CustomerID = c.CustomerID
    left JOIN Person p ON p.PersonID = cp.PersonID
    LEFT JOIN Branches b ON b.BranchId = a.BranchID
    where a.ParentAccountID IS NULL 
    AND {search_filter_string}"""
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