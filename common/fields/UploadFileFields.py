import os

from django.conf import settings
from django.db.models import FileField
from django.db.models.fields.files import FieldFile

MAX_LENGTH = 'max_length'

__all__ = (
    'UploadFileField',
    'UploadFileMixin',
)


class UploadFileMixin:
    """
    Mixin for handling files already uploaded to upload directory
    Also changes default max_length to 255
    """

    def __init__(self, **kwargs):
        kwargs.setdefault(MAX_LENGTH, settings.FILE_NAME_LENGTH)
        super().__init__(**kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get(MAX_LENGTH) == settings.FILE_NAME_LENGTH:
            del kwargs[MAX_LENGTH]
        return name, path, args, kwargs

    def _save_file(self, file):
        path, file_name = os.path.split(file.name)
        if path == settings.FILE_UPLOAD_DIR:
            file_obj = file.file
            file.save(file_name, file_obj, False)

    def pre_save(self, model_instance, add):
        file: FieldFile = super().pre_save(model_instance, add)
        if file.name:
            self._save_file(file)
        return file


class UploadFileField(UploadFileMixin, FileField):
    pass
