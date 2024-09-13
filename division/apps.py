from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DivisionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'division'
    verbose_name = _('division')
