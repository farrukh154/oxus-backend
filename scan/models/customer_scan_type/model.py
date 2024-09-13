from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from common.mixinUid import UidMixin
from common.fields import create_char_field

class CustomerScanType(AbstractBaseModel, UidMixin):
    class Meta:
        verbose_name = _('customer scans types')
        verbose_name_plural = _('customer scans types')

    name = create_char_field(
        max_length=255,
        verbose_name=_("name"),
    )


    def __str__(self):
        return self.name
