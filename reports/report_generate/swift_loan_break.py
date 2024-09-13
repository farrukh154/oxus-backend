import json
from django.http import HttpResponse
import pandas as pd
import time

from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from common.utils import check_permission

from .utils import get_uniq_report_name
from .utils import get_filename_with_path
from .utils import set_report_header
from .utils import create_report_history
from .utils import get_abacus_branches

from ..models import Report
from ..models.report.model import REPORT_SWIFT_LOAN_BREAK
from ..models.report.model import REPORT_MODEL
from request_credit.models import RequestCredit

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def swift_loan_break(request):
    check_permission(request.user, Report, f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN_BREAK}_{REPORT_MODEL}')
    report_name = REPORT_SWIFT_LOAN_BREAK.replace('-', '_')
    report_version = '20240325'
    start_time = time.time()


    data = json.loads(request.body.decode("utf-8")) if request.body else {}
    date_start = data.get("date_start", None )
    date_end = data.get("date_end", None )
    branches = data.get("branch", '')
    branch_ids = [
        int(branch_id) for branch_id in branches.split(",") if branch_id.isdigit()
    ]
    branches_for_report = get_abacus_branches(branches)

    uniq_report_name = get_uniq_report_name(report_name)
    file_name_with_path = get_filename_with_path(uniq_report_name)

    credits = RequestCredit.objects.filter(created__gte=date_start, created__lte=date_end, branch_id__in=branch_ids)
    if not credits.exists():
        return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "За отчетный период нет записей"}), content_type="application/json")

    df = pd.DataFrame(list(credits.values(
        'id',
        'status__name',
        'created',
        'created_by__first_name',
        'created_by__last_name',
        'customer__name',
        'customer__birthday',
        'customer__INN',
        'customer__passport',
        'branch__description',
        'customer__gender',
        'approve_amount',
        'approve_installment',
        'approve_currency_new__description',
    )))

    df['created'] = df['created'].dt.tz_localize(None)
    df['Created by'] = df['created_by__first_name'] + ' ' + df['created_by__last_name']
    df = df.rename(columns={
        'status__name': 'Status',
        'name': 'Client name',
        'branch__description': 'Branch',
        'approve_amount': 'Amount',
        'approve_installment': 'Installment',
        'approve_currency_new__description': 'Currency',
    })
    df['Count'] = [1 if x else 0 for x in df['Status']]
    df = df.drop('created_by__first_name', axis=1)
    df = df.drop('created_by__last_name', axis=1)

    writer = pd.ExcelWriter(file_name_with_path, engine='xlsxwriter')
    pivot_branch = df.pivot_table(
        index=['Branch'],
        values=['Amount', 'Count'],
        aggfunc='sum',
        margins=True
    )
    pivot_branch.to_excel(writer, sheet_name=report_name, startrow=8)

    pivot_status = df.pivot_table(
        index=['Status'],
        values=['Amount', 'Count'],
        aggfunc='sum',
        margins=True
    )
    pivot_status.to_excel(writer, sheet_name='Status')

    pivot_created_by = df.pivot_table(
        index=['Created by'],
        values=['Amount', 'Count'],
        aggfunc='sum',
        margins=True
    )
    pivot_created_by.to_excel(writer, sheet_name='Created by')

    workbook  = writer.book
    worksheet = set_report_header(workbook, writer, report_name, report_version)

    format_date = workbook.add_format({'num_format': 'd.mm.yyyy'})
    worksheet.write('D5', 'Date start:')
    worksheet.write('E5', date_start, format_date)
    worksheet.write('G5', 'Date end:')
    worksheet.write('H5', date_end, format_date)
    worksheet.write('D6', 'Branches:')
    worksheet.write('E6', branches_for_report[1])

    writer.close()

    create_report_history(
        f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN_BREAK}',
        round(time.time() - start_time),
        request,
        uniq_report_name,
    )

    return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "Отчет сформирован успешно"}), content_type="application/json")
