import json
from django.http import HttpResponse
import pandas as pd
import time

from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from common.utils import check_permission
from oxus.utils.try_get_attr import try_get_attr

from .utils import get_uniq_report_name
from .utils import get_filename_with_path
from .utils import set_report_header
from .utils import create_report_history
from .utils import get_abacus_branches

from ..models import Report
from ..models.report.model import REPORT_SWIFT_LOAN_CLIENT_DECISION
from ..models.report.model import REPORT_MODEL
from request_credit.models import ClientDecision

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def swift_loan_client_decision(request):
    check_permission(request.user, Report, f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN_CLIENT_DECISION}_{REPORT_MODEL}')
    report_name = REPORT_SWIFT_LOAN_CLIENT_DECISION.replace('-', '_')
    report_version = '20240712'
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

    decisions = ClientDecision.objects.filter(created__gte=date_start, created__lte=date_end, customer__branch_id__in=branch_ids)
    if not decisions.exists():
        return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "За отчетный период нет записей"}), content_type="application/json")

    list_of_data = []
    for rec_no, decision in enumerate(decisions.iterator(chunk_size=10), 1):
        list_of_data.append({
            'Филиал/ЦМО': try_get_attr(lambda: decision.customer.branch.description),
            'ФИО клиента': try_get_attr(lambda: decision.customer.name),
            'ИНН': try_get_attr(lambda: decision.customer.INN),
            'ID клиента': try_get_attr(lambda: decision.customer.client_ID),
            'Номер телефона 1': try_get_attr(lambda: decision.customer.phone1),
            'Номер телефона 2': try_get_attr(lambda: decision.customer.phone2),
            'Номер телефона 3': try_get_attr(lambda: decision.customer.phone3),
            'Статус': 'Активный' if decision.active_in_abacus else 'Не активный',
            'Оператор': f"{try_get_attr(lambda: decision.created_by.last_name)} {try_get_attr(lambda: decision.created_by.first_name)}",
            'Дата обработки': decision.created.date(),
            'Время обработки': decision.created.strftime("%H:%M"),
            "Канал поступления заявки": decision.get_application_receipt_channel_display(),
            'Решение клиента': decision.get_client_decision_display(),
            'Причина отказа': decision.get_client_refused_display(),
            "Недозвон": decision.get_missed_call_display(),
            'Ответ/Комментарии клиента': decision.customer_response,
            'Комментарии сотрудника': decision.employee_comments,
        })
    df = pd.DataFrame(list_of_data)

    df.index += 1
    writer = pd.ExcelWriter(file_name_with_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=report_name, startrow=7)

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
        f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN_CLIENT_DECISION}',
        round(time.time() - start_time),
        request,
        uniq_report_name,
    )

    return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "Отчет сформирован успешно"}), content_type="application/json")
