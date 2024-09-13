from django.db.models import CharField
from .UploadFileFields import UploadFileField
from .UploadFileFields import UploadFileMixin

__all__ = (
    'UploadFileField',
)

DEFAULT_PARAMS_CHAR_FIELD = {
    'null': False,
    'default': '',
}

def create_char_field(**kwargs):
    return CharField(**{**DEFAULT_PARAMS_CHAR_FIELD, **kwargs})
