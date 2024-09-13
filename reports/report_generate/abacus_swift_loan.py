import pypyodbc as odbc
import json
from django.http import HttpResponse
import pandas as pd
import time

from common.abacus.connection import connection_string
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from common.utils import check_permission

from .utils import get_uniq_report_name
from .utils import get_filename_with_path
from .utils import create_or_alter_report_function
from .utils import set_report_header
from .utils import create_report_history

from ..models import Report
from ..models.report.model import REPORT_ABACUS_SWIFT_LOAN
from ..models.report.model import REPORT_MODEL

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def abacus_swift_loan(request):
    check_permission(request.user, Report, f'{REPORT_MODEL}-{REPORT_ABACUS_SWIFT_LOAN}_{REPORT_MODEL}')
    report_name = REPORT_ABACUS_SWIFT_LOAN.replace('-', '_')
    report_version = '20240408'
    start_time = time.time()


    data = json.loads(request.body.decode("utf-8")) if request.body else {}
    date = data.get("date", None )

    create_or_alter_report_function(report_name)
    uniq_report_name = get_uniq_report_name(report_name)
    file_name_with_path = get_filename_with_path(uniq_report_name)

    conn = odbc.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute(f"select * from {report_name}('{date}')")
    if cursor.rowcount == 0:
        return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "Отчет пустой"}), content_type="application/json")

    df = pd.DataFrame((tuple(t) for t in cursor))
    df.index += 1
    df.columns = [column[0] for column in cursor.description]
    writer = pd.ExcelWriter(file_name_with_path, engine='xlsxwriter')
    df = df.rename(columns={
        'branch': 'Филиал',
        'subbranch': 'ЦМО',
        'name': 'ФИО',
        'gender': 'Гендер',
        'age': 'Возраст',
        'customerid': 'ID',
        'passport': 'Серия паспорта',
        'inn': 'ИНН',
        'phone': 'Номер телефона 1',
        'phone2': 'Номер телефона 2',
        'phone3': 'Номер телефона 3',
        'status': 'Статус кредита',
        'disbursedintjs': 'Выданная сумма TJS',
        'currency': 'Валюта',
        'interestrate': '% ставка',
        'cycle': 'Количество циклов',
        'olbintjs': 'Остаток кредита TJS',
        'startdate': 'Дата выдачи',
        'closedate': 'Дата закрытия план',
        'closedatefact': 'Дата закрытия факт',
        'numberdelinquency': 'Количество просрочек за последние 365 дней',
        'daynumberdelinquency': 'Количество дней в просрочке за 365 дней',
        'productactivity': 'Сектор деятельности',
        'clientactivity1': 'Деятельность клиента 1',
        'clientactivity2': 'Деятельность клиента 2',
        'product': 'Продукт',
        'industrycode': 'Цель кредита',
        'methodofanalysis': 'Метод анализа',
        'loanofficerifincollector': 'Коллектор',
        'restructured': 'Реструктуризация',
        'late_days': 'Текущая просрочка',
        'dateofcortcases': 'Судебный',
    })
    df.to_excel(writer, sheet_name=report_name, startrow=7)

    workbook  = writer.book
    worksheet = set_report_header(workbook, writer, report_name, report_version)

    format_date = workbook.add_format({'num_format': 'd.mm.yyyy'})
    worksheet.write('D5', 'Report date:')
    worksheet.write('E5', date, format_date)

    writer.close()

    create_report_history(
        f'{REPORT_MODEL}-{REPORT_ABACUS_SWIFT_LOAN}',
        round(time.time() - start_time),
        request,
        uniq_report_name,
    )

    cursor.close()
    conn.close()
    return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "Отчет сформирован успешно"}), content_type="application/json")
