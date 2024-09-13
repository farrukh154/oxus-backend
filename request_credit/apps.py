from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class RequestCreditConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'request_credit'
    verbose_name = _('request credit')