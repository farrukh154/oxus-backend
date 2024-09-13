from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    code = models.TextField(verbose_name=_("Code"), max_length=100)
    description = models.TextField(verbose_name=_("Description"), max_length=350)

    def __str__(self):
        return self.code


    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("Accounts")
