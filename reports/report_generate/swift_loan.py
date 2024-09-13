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
from ..models.report.model import REPORT_SWIFT_LOAN
from ..models.report.model import REPORT_MODEL
from request_credit.models import RequestCredit

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def swift_loan(request):
    check_permission(request.user, Report, f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN}_{REPORT_MODEL}')
    report_name = REPORT_SWIFT_LOAN.replace('-', '_')
    report_version = '20240605'
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

    credits = RequestCredit.objects.filter(created__gte=date_start, created__lte=date_end, branch_id__in=branch_ids, underwriter_status__isnull=False)
    if not credits.exists():
        return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "За отчетный период нет записей"}), content_type="application/json")

    list_of_data = []
    for rec_no, credit in enumerate(credits.iterator(chunk_size=10), 1):
        list_of_data.append({
            'Код заявки': credit.id,
            'Филиал/ЦМО': try_get_attr(lambda: credit.branch.description),
            'Статус': try_get_attr(lambda: credit.underwriter_status.name),
            'Причина отказа (Андерайтер)': try_get_attr(lambda: credit.rejection_reason.name),
            'Андеррайтер': f"{try_get_attr(lambda: credit.underwriter_status_change_by.last_name)} {try_get_attr(lambda: credit.underwriter_status_change_by.first_name)}",
            'Дата создания заявки': credit.created,
            'Дата создания протокола': credit.underwriter_status_change_date,
            'Сумма кредита в заявке': credit.request_amount,
            'Сумма кредита в протоколе': credit.approve_amount,
            'Срок кредита': credit.approve_installment,
            'Процентная ставка': credit.approve_interest,
            'Льготный период': credit.approve_grace_period,
            'Внутренний рейтинг': credit.get_rating_internal_display(),
            'Внешний рейтинг': credit.get_rating_external_display(),
            'ФИО клиента': try_get_attr(lambda: credit.customer.name),
            'Номер паспорта': try_get_attr(lambda: credit.customer.passport),
            'ИНН': try_get_attr(lambda: credit.customer.INN),
            'Пол': try_get_attr(lambda: credit.customer.get_gender_display()),
            'Дата рождения': try_get_attr(lambda: credit.customer.birthday),
            'Категория деятельности': try_get_attr(lambda: credit.economic_activity.name),
            'Тип деятельности': try_get_attr(lambda: credit.economic_activity_type.name),
            'Номер телефона 1': try_get_attr(lambda: credit.customer.phone1),
            'Номер телефона 2': try_get_attr(lambda: credit.customer.phone2),
            'Валюта кредита': try_get_attr(lambda: credit.approve_currency_new.description),
            'Цель кредита': try_get_attr(lambda: credit.credit_purpose.name),
            'Сфера вложения': try_get_attr(lambda: credit.get_investment_sector_display()),
            'ID клиента Abacus': credit.customer.client_ID,
            'СОК': f"{try_get_attr(lambda: credit.created_by.last_name)} {try_get_attr(lambda: credit.created_by.first_name)}",
            'Условия в протоколе': try_get_attr(lambda: credit.get_approve_condition_display()),
            'Решение': credit.get_result_display(),
            'Код контракта': credit.credit_ID,
            'Причина отказа': try_get_attr(lambda: credit.client_rejection_reason.name),
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
        f'{REPORT_MODEL}-{REPORT_SWIFT_LOAN}',
        round(time.time() - start_time),
        request,
        uniq_report_name,
    )

    return HttpResponse(status=HTTP_200_OK, content=json.dumps({"message": "Отчет сформирован успешно"}), content_type="application/json")
