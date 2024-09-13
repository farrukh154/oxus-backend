
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
def swift_search_client(req):
  json_data = json.loads(req.body)
  search_string = ''
  if 'client_ID' in json_data:
    search_string += f"c.CustomerID={json_data['client_ID']}"
  if 'credit_ID' in json_data:
    search_string += f"a.AccountNumber LIKE N'%{json_data['credit_ID']}%'"
  if 'name' in json_data:
    if search_string:
      search_string += ' AND '
    search_string += f"c.Name LIKE N'%{json_data['name']}%'"
  if 'passport' in json_data:
    if search_string:
      search_string += ' AND '
    search_string += f"p.SocialSecurityNumber LIKE N'%{json_data['passport']}%'"
  if 'INN' in json_data:
    if search_string:
      search_string += ' AND '
    search_string += f"p.DrivingLicenceNumber LIKE N'%{json_data['INN']}%'"

  conn = odbc.connect(connection_string)
  cursor = conn.cursor()
  cursor.execute(
    f"""SELECT TOP 10
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
      p.Telephone1 AS phone2,
      p.Telephone3 AS phone3,
      CONCAT(udfl.Value, ' ', udfl2.Value) AS passport_details
      FROM Customer c
      INNER JOIN CustomerPerson cp ON cp.CustomerID = c.CustomerID
      INNER JOIN Person p ON p.PersonID = cp.PersonID AND p.DrivingLicenceNumber <> 'NULL'
      LEFT JOIN Branches b ON b.BranchId = c.BranchId
      LEFT JOIN CUAccount a ON a.CustomerID = c.CustomerID
        AND a.CUAccountID = (SELECT MAX(az.CUAccountID) FROM CUAccount az WHERE az.CustomerID = a.CustomerID AND az.ParentAccountID IS NULL)
        AND a.AccountNumber NOT LIKE '%.%'
      LEFT JOIN CustomerAddress ca1 ON ca1.CustomerID = c.CustomerID AND ca1.AddressTypeID = 1
      LEFT JOIN Address addr1 ON addr1.AddressID = ca1.AddressID
      LEFT JOIN CustomerAddress ca2 ON ca2.CustomerID = c.CustomerID AND ca2.AddressTypeID = 2
      LEFT JOIN Address addr2 ON addr2.AddressID = ca2.AddressID
      LEFT JOIN UserDefinedFieldLinks udfl ON udfl.CustomerID = c.CustomerID AND udfl.UserDefinedFieldID = 3
      LEFT JOIN UserDefinedFieldLinks udfl2 ON udfl2.CustomerID = c.CustomerID AND udfl2.UserDefinedFieldID = 4
    WHERE {search_string}"""
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