from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from django.db import models
from division.models.branch.model import Branch
from division.models.district.model import District
from django.core.validators import MinLengthValidator
from common.constants import STANDARD_MALE_FEMALE_CHOICE


class Customer(AbstractBaseModel):
    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    name = create_char_field(
        max_length=255,
        verbose_name=_("name"),
    )
    birthday = models.DateField(_("birthday"), null=True, blank=True)
    
    gender = models.CharField(
        max_length=50,
        verbose_name="gender",
        choices=STANDARD_MALE_FEMALE_CHOICE,
        null=True,
        blank=True,
    )

    client_ID = models.BigIntegerField(_("Client ID"), null=True, blank=True)

    INN = create_char_field(max_length=9, validators=[MinLengthValidator(9)], verbose_name=_("INN"), null=True, blank=True,unique=True)

    passport = create_char_field(
        max_length=255, verbose_name=_("Passport"), null=True, blank=True
    )

    passport_date = models.DateField(_("passport_date"), null=True, blank=True)


    passport_details = create_char_field(
        max_length=255, verbose_name=_("Passport details"), null=True, blank=True
    )

    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, null=True, blank=True, verbose_name=_("branch"),)

    registration_address = models.ForeignKey(
        District,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("registration address"),
        related_name="customer_registration_address",
    )

    registration_address_street = create_char_field(
        max_length=255,
        verbose_name=_("registration address street"),
        null=True,
        blank=True,
    )

    address = models.ForeignKey(
        District,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("address"),
        related_name="customer_address",
    )

    address_street = create_char_field(
        max_length=255,
        verbose_name=_("address street"),
        null=True,
        blank=True,
    )

    phone1 = create_char_field(
        max_length=15, verbose_name=_("phone 1"), null=True, blank=True
    )
    phone2 = create_char_field(
        max_length=15, verbose_name=_("phone 2"), null=True, blank=True
    )

    phone3 = create_char_field(
        max_length=15, verbose_name=_("phone 3"), null=True, blank=True
    )

    family_status = models.CharField(
        max_length=50,
        verbose_name=_("family status"),
        choices=[
            ("married", "Оиладор"),
            ("single", "Мучаррад"),
            ("separated", "Чудошуда"),
            ("widow", "Бевазан/Мард"),
        ],
        null=True,
        blank=True,
    )

    spouse = create_char_field(
        max_length=255, verbose_name=_("spouse"), null=True, blank=True
    )

    spouse_phone = create_char_field(
        max_length=15, verbose_name=_("spouse phone"), null=True, blank=True
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.INN}"
