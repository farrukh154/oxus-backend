from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from common.mixins.WhoDidItMixin import WhoDidItMixin
from scan.models.customer_scan_type import CustomerScanType
from common.utils import create_dir_by_path
from os.path import sep as os_path_sep
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from scan.utils.utils import only_pdf, compress_pdf
from model_utils import FieldTracker
from common.fields import UploadFileField



def get_customer_scan_path(instance, filename):
    path_to_docs = os_path_sep.join(['customer_scan'])
    create_dir_by_path(path_to_docs)
    return os_path_sep.join([path_to_docs, str(instance.abacus_id), filename])


class CustomerScan(AbstractBaseModel, WhoDidItMixin):
    class Meta:
        verbose_name = _('customer scans')
        verbose_name_plural = _('customer scans')

    file = UploadFileField(
        verbose_name="file",
        upload_to=get_customer_scan_path,
        validators=[only_pdf]
    )

    abacus_id = models.IntegerField(
        verbose_name='abacus_ID',
        blank=True,
        null=True,
    )

    type = models.ForeignKey(
       CustomerScanType, on_delete=models.CASCADE
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