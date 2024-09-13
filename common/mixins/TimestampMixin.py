from django.db import models
from django.utils.translation import gettext_lazy as _


__all__ = ('TimestampMixin',)


class TimestampMixin(models.Model):
    class Meta:
        ordering = ('updated',)
        abstract = True

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'), null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated'), null=True)
