import pypyodbc as odbc
import json
from django.http import HttpResponse
from common.abacus.connection import connection_string
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def terminal_payment_change_date(request):
    data = json.loads(request.body.decode("utf-8")) if request.body else {}
    selected_id = data.get("selectedId", None)
    selected_date = data.get("selectedDate", None)

    conn = odbc.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute(f"UPDATE OTJ_TerminalPay SET PayDate='{selected_date}' WHERE id={selected_id}")

    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse(status=HTTP_200_OK, content=json.dumps('Ok'), content_type="application/json")
