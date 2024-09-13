import pypyodbc as odbc
import json
from django.http import HttpResponse
from common.abacus.connection import connection_string
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def terminal_payment_change_contract(request):
    data = json.loads(request.body.decode("utf-8")) if request.body else {}
    selected_contract_code = data.get("selectedContractCode", None)
    selected_contract_code_id = data.get("selectedContractCodeId", None)

    conn = odbc.connect(connection_string)

    cursor_s = conn.cursor()
    cursor_s.execute(f"SELECT AccountNumber FROM CUAccount where AccountNumber like N'%{selected_contract_code}%'")
    contract_code_found = len(cursor_s.fetchall())
    if contract_code_found == 0:
        raise ValidationError("Contract code not found.")
    cursor_s.close()

    cursor = conn.cursor()
    cursor.execute(f"UPDATE OTJ_TerminalPay SET AccountNumber='{selected_contract_code}' WHERE id={selected_contract_code_id}")
    conn.commit()
    cursor.close()

    conn.close()
    return HttpResponse(status=HTTP_200_OK, content=json.dumps('Ok'), content_type="application/json")

