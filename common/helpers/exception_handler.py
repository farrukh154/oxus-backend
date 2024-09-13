from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if isinstance(exc, ValidationError):
        message = exc.message if hasattr(exc, 'message') else '<br/>'.join(exc.messages)
        response = HttpResponse(message, content_type="text/html; charset=utf-8")
        response.status_code = 500
        return response
    return exception_handler(exc, context)
