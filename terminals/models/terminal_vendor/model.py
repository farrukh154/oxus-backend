from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel


class Terminal_Vendor(AbstractBaseModel):
    class Meta:
        verbose_name = _("terminal vendor")
        verbose_name_plural = _("terminal vendors")

    name = create_char_field(
        max_length=255,
        verbose_name=_("name"),
        unique=True,
    )

    def __str__(self):
        return self.name
