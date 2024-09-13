import os
import json

from weasyprint import HTML
from django.http import HttpResponse
from oxus.settings import BASE_DIR
from oxus.settings import BASE_URL
from scoring.models.crif import CRIF
from django.template.loader import render_to_string


def crif_generate_client_report(request, id):
    crif = CRIF.objects.get(id=id)
    path_to_template = os.path.join(BASE_DIR, "scoring/templates/crif_report_print.html")
    path_to_template_error = os.path.join(BASE_DIR, "scoring/templates/crif_error_print.html")
    data = json.loads(crif.data)

    if 'Error' in data:
        html_string = render_to_string(path_to_template_error, {
            'data': data,
        })
        pdf_file = HTML(string=html_string, base_url=BASE_URL).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'filename="crif_report_{id}.pdf"'
        return response


    matched = data['Subject']['Matched']['FlgMatched']
    subject = data['Subject']['Matched'] if matched == '1' else data['Subject']['Inquired']
    if 'Company' in subject:
        subject_details = subject['Company']
        is_company = True
    else:
        subject_details = subject['Person']
        is_company = False

    if isinstance(subject_details.get('Documents', {}), dict) and subject_details.get('Documents', {}).get('Main'):
        passport = subject_details.get('Documents', {}).get('Main')
    elif passport := subject_details.get('Documents'):
        passport = subject_details.get('Documents')

    html_string = render_to_string(path_to_template, {
        'crif': crif,
        'data': data,
        'is_company': is_company,
        'subject': subject,
        'subject_details': subject_details,
        'find': 'Субъект найден' if matched == '1' else 'Субъект не найден',
        'passport': passport,
    })
    pdf_file = HTML(string=html_string, base_url=BASE_URL).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="crif_report_{id}.pdf"'
    return response