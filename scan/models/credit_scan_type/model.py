from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from common.mixinUid import UidMixin
from common.fields import create_char_field

class CreditScanType(AbstractBaseModel, UidMixin):
    class Meta:
        verbose_name = _('credits scans types')
        verbose_name_plural = _('credits scans types')

    name = create_char_field(
        max_length=255,
        verbose_name=_("name"),
    )


    def __str__(self):
        return self.name
