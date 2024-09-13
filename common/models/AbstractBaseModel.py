from ..mixins import TimestampMixin


__all__ = ('AbstractBaseModel',)


class AbstractBaseModel(TimestampMixin):
    class Meta(TimestampMixin.Meta):
        abstract = True
