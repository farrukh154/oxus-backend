from django.utils.translation import gettext_lazy as _
from common.fields import create_char_field
from common.models.AbstractBaseModel import AbstractBaseModel
from common.mixinUid import UidMixin

UID_CRIF_CREDIT = 'CRIF-CREDIT'
UID_CRIF_GUARANTOR = 'CRIF-GUARANTOR'
class ScoringType(AbstractBaseModel, UidMixin):
    class Meta:
        verbose_name = _("Scoring type")
        verbose_name_plural = _("Scoring types")

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
        null=True,
        blank=True
    )


    def __str__(self):
        return f"{self.name}"
