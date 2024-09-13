import os
from datetime import datetime

from weasyprint import HTML
from django.http import HttpResponse
from oxus.settings import BASE_DIR
from oxus.settings import BASE_URL
from request_credit.models.r_credit import RequestCredit
from common.helpers.number_helper import number_to_words_tj
from credits.helpers.loan_payment_schedule import LoanPaymentSchedule

def print_protocol(request, id):
    request_credit = RequestCredit.objects.get(id=id)
    path_to_template = os.path.join(BASE_DIR, "request_credit/templates/protocol_print.html")
    from django.template.loader import render_to_string
    monthly_profit = (request_credit.monthly_income or 0) - (request_credit.monthly_household_expenses or 0) - (request_credit.monthly_payment_loans or 0)
    result = LoanPaymentSchedule().calculate(
        request_credit.approve_amount,
        request_credit.approve_installment,
        request_credit.approve_grace_period,
        request_credit.approve_interest
    )
    try:
        monthly_payment = result[request_credit.approve_grace_period + 1].get_payment_amount()
    except:
        monthly_payment = 0
    html_string = render_to_string(path_to_template, {
        'credit': request_credit,
        'amount_str': number_to_words_tj(request_credit.approve_amount),
        'monthly_profit': monthly_profit,
        'current_date': datetime.today().strftime('%d.%m.%Y'),
        'monthly_payment': round(monthly_payment, 2),
        'coefficient': round(monthly_profit / monthly_payment, 2) if monthly_payment else 0
    })
    pdf_file = HTML(string=html_string, base_url=BASE_URL).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="protocol_print_{id}.pdf"'
    return response