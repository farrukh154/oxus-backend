from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models


class Region(AbstractBaseModel):
    class Meta:
        verbose_name = _("regions")
        verbose_name_plural = _("regions")

    abacus_id = models.BigIntegerField("abacus id", default=0)

    name = create_char_field(
        max_length=255, verbose_name=_("name"), null=True, blank=True
    )

    active = models.BooleanField("active", default=True)

    def __str__(self):
        return self.name or "region"
