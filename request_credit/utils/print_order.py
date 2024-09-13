import os
from datetime import datetime

from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.http import HttpResponse
from oxus.settings import BASE_DIR
from oxus.settings import BASE_URL
from request_credit.models.r_credit import RequestCredit
from common.helpers.number_helper import number_to_words_tj
from common.helpers.number_helper import number_to_words_drob_tj
from django.template.loader import render_to_string

def print_order(request, id):
    request_credit = RequestCredit.objects.get(id=id)
    path_to_template = os.path.join(BASE_DIR, "request_credit/templates/order_print.html")

    html_string = render_to_string(path_to_template, {
        'credit': request_credit,
        'amount_str': number_to_words_tj(request_credit.approve_amount),
        'interest_str': number_to_words_drob_tj(request_credit.approve_issue_fee),
    })
    pdf_file = HTML(string=html_string, base_url=BASE_URL).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="order_print_{id}.pdf"'
    return response