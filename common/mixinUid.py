from django.db import models

__all__ = ('UidMixin',)

class UidMixin(models.Model):
    uid = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        help_text='Unique identifier for reference to record from code. Do not change if set!',
    )
    class Meta:
        abstract = True
