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
from .utils import get_abacus_branches
from .utils import get_abacus_currencies
from .utils import create_or_alter_report_function
from .utils import set_report_header
from .utils import create_report_history

from ..models import Report
from ..models.report.model import REPORT_ABACUS_ACTIVE_LOAN
from ..models.report.model import REPORT_MODEL

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def abacus_active_loan(request):
    check_permission(request.user, Report, f'{REPORT_MODEL}-{REPORT_ABACUS_ACTIVE_LOAN}_{REPORT_MODEL}')
    report_name = REPORT_ABACUS_ACTIVE_LOAN.replace('-', '_')
    report_version = '20240322'
    start_time = time.time()


    data = json.loads(request.body.decode("utf-8")) if request.body else {}
    date = data.get("date", None )
    branches = get_abacus_branches(data.get("branch", ''))
    currencies = get_abacus_currencies(data.get("currency", ''))

    create_or_alter_report_function(report_name)
    uniq_report_name = get_uniq_report_name(report_name)
    file_name_with_path = get_filename_with_path(uniq_report_name)

    conn = odbc.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute(f"select * from {report_name}('{date}', '{currencies[0]}', '{branches[0]}')")
    if cursor.rowcount == 0:
        return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "Отчет пустой"}), content_type="application/json")

    df = pd.DataFrame((tuple(t) for t in cursor))
    df.columns = [column[0] for column in cursor.description]
    df['Individual'] = [1 if x == 1 else 0 for x in df['customertypeid']]
    df['Group'] = [1 if x == 8 else 0 for x in df['customertypeid']]
    df['Corporate'] = [1 if x == 4 else 0 for x in df['customertypeid']]
    df['Contracts'] = [1 if x > 0 else 0 for x in df['culoanid']]
    df['In Group'] = [x if x > 1 else 0 for x in df['groupcount']]
    df = df.rename(columns={
        'branch': 'Branch',
        'sub branch': 'Sub Branch',
        'olb tjs': 'OLB in TJS',
        'olb usd': 'OLB in USD',
        'groupcount': 'Clients',
        'product': 'Product',
        'client activity1': 'Client Activity',
    })
    writer = pd.ExcelWriter(file_name_with_path, engine='xlsxwriter')

    pivot_branch = df.pivot_table(
        index=['Branch'],
        values=['Contracts', 'Individual', 'Group', 'Corporate', 'Clients', 'In Group', 'OLB in TJS', 'OLB in USD'],
        aggfunc='sum',
        margins=True
    )
    pivot_branch.to_excel(writer, sheet_name=report_name, startrow=8)

    pivot_subbranch = df.pivot_table(
        index=['Sub Branch'],
        values=['Contracts', 'Individual', 'Group', 'Corporate', 'Clients', 'In Group', 'OLB in TJS', 'OLB in USD'],
        aggfunc='sum',
        margins=True
    )
    pivot_subbranch.to_excel(writer, sheet_name='Sub Branch')

    pivot_product = df.pivot_table(
        index=['Product'],
        values=['Contracts', 'Individual', 'Group', 'Corporate', 'Clients', 'In Group', 'OLB in TJS', 'OLB in USD'],
        aggfunc='sum',
        margins=True
    )
    pivot_product.to_excel(writer, sheet_name='Product')

    pivot_product = df.pivot_table(
        index=['Client Activity'],
        values=['Contracts', 'Individual', 'Group', 'Corporate', 'Clients', 'In Group', 'OLB in TJS', 'OLB in USD'],
        aggfunc='sum',
        margins=True
    )
    pivot_product.to_excel(writer, sheet_name='Activity')

    workbook  = writer.book
    worksheet = set_report_header(workbook, writer, report_name, report_version)

    format_date = workbook.add_format({'num_format': 'd.mm.yyyy'})
    worksheet.write('D5', 'Report date:')
    worksheet.write('E5', date, format_date)
    worksheet.write('G5', 'Currencies:')
    worksheet.write('H5', currencies[1])
    worksheet.write('D6', 'Branches:')
    worksheet.write('E6', branches[1])

    writer.close()

    create_report_history(
        f'{REPORT_MODEL}-{REPORT_ABACUS_ACTIVE_LOAN}',
        round(time.time() - start_time),
        request,
        uniq_report_name,
    )

    cursor.close()
    conn.close()
    return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "Отчет сформирован успешно"}), content_type="application/json")
