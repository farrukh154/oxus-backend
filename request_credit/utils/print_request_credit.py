import os
from datetime import datetime
from weasyprint import HTML, CSS
from django.http import HttpResponse
from oxus.settings import BASE_DIR
from oxus.settings import BASE_URL
from request_credit.models.r_credit import RequestCredit

def print_request_credit(request, id):
    request_credit = RequestCredit.objects.get(id=id)
    path_to_template = os.path.join(
        BASE_DIR, "request_credit/templates/request_credit.html"
    )
    from django.template.loader import render_to_string

    html_string = render_to_string(
        path_to_template,
        {
            "credit": request_credit,
            "current_date": datetime.today().strftime("%d.%m.%Y"),
        },
    )
    pdf_file = HTML(string=html_string, base_url=BASE_URL).write_pdf()
    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f'filename="request_credit_{id}.pdf"'
    return response
