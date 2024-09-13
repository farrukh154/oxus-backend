from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from common.mixins.WhoDidItMixin import WhoDidItMixin
from scan.models.credit_scan_type import CreditScanType
from common.utils import create_dir_by_path
from os.path import sep as os_path_sep
from common.fields import UploadFileField

from model_utils import FieldTracker
from scan.utils.utils import only_pdf, compress_pdf


def get_credit_scan_path(instance, filename):
    path_to_docs = os_path_sep.join(['credit_scan'])
    create_dir_by_path(path_to_docs)
    return os_path_sep.join([path_to_docs, str(instance.abacus_id), filename])


class CreditScan(AbstractBaseModel, WhoDidItMixin):
    class Meta:
        verbose_name = _('Credit Scan')
        verbose_name_plural = _('Credit Scans')

    file = UploadFileField(
        verbose_name=_("File"),
        upload_to=get_credit_scan_path,
        validators=[only_pdf]
    )

    abacus_id = models.IntegerField(
        verbose_name=_('Abacus ID'),
        blank=True,
        null=True,
    )

    type = models.ForeignKey(
        CreditScanType, on_delete=models.CASCADE
    )

    tracker = FieldTracker()

    description = models.CharField(
        max_length=255,
        verbose_name=_("description"),
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        file_has_changed = self.tracker.has_changed('file')
        super().save(*args, **kwargs)
        if file_has_changed and self.file:
            compress_pdf(self.file.path)