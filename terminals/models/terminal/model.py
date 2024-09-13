from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel

class Terminal(AbstractBaseModel):
    class Meta:
        verbose_name = _('terminal')
        verbose_name_plural = _('terminals')

        permissions = [
            ("can-change-terminal-payments_terminal", "Can change terminal payments"),
        ]

    name = create_char_field(
        max_length=255,
        verbose_name=_('name'),
        unique=True,
    )

    def __str__(self):
        return self.name
