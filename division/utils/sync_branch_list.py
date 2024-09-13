from django.http import HttpResponse
from rest_framework.status import HTTP_200_OK
import pypyodbc as odbc
from common.abacus.connection import connection_string
from division.models.branch import Branch

def sync_branch_list(data):

    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('''select b.BranchID, b.Name, b.Description, b.Code, ISNULL(ob.Branch, 'not set') as regbranch, b.Active from Branches as b
        left join OTJ_Branches as ob on b.BranchID = ob.OTJ_BranchID''')
    while True:
        row = cursor.fetchone()
        if not row:
            break
        Branch.objects.update_or_create(abacus_id = row['branchid'], defaults={
            'abacus_id': row['branchid'],
            'active': row['active'],
            'name': row['name'],
            'description': row['description'],
            'code': row['code'],
            'regional_branch': row['regbranch'],
        })

    return HttpResponse(status=HTTP_200_OK, content='Синхронизация прошла успешно')