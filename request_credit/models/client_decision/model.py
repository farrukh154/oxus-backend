from common.fields import create_char_field
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from common.mixins import WhoDidItMixin
from django.db import models


class ClientDecision(AbstractBaseModel, WhoDidItMixin):
    class Meta:
        verbose_name = _('Client decision')
        verbose_name_plural = _('Client decisions')

    application_receipt_channel = models.CharField(
        max_length=50,
        verbose_name="application receipt channel",
        choices=[
            ("call-to-call-center", "Звонок в Колл-центр"),
            ("online", "Онлайн заявка"),
            ("call-from-call-center", "Звонок от Колл-центра"),
        ],
        null=True,
        blank=True,
    )

    client_decision = models.CharField(
        max_length=50,
        verbose_name="client decision",
        choices=[
            ("agree", "Согласен"),
            ("refused", "Отказался"),
            ("will-think", "Подумает"),
            ("missed-call", "Недозвон"),
            ("no-information", "Нет информации"),
        ],
        null=True,
        blank=True,
    )

    customer_response = create_char_field(
        max_length=255,
        verbose_name=_("customer response/comments"),
        null=True,
        blank=True,
    )

    employee_comments = create_char_field(
        max_length=255,
        verbose_name=_("employee comments"),
        null=True,
        blank=True,
    )

    client_refused = models.CharField(
        max_length=50,
        verbose_name="client refused",
        choices=[
            ("not-need-loan", "Не нуждается в кредите"),
            ("commission-fee", "Наличие комиссионного сбора"),
            ("high-interest-rates", "Высокие процентные ставки"),
            ("client-wants-larger-loan-amount", "Клиент хочет большую сумму кредита"),
            ("received-loan", "Получил кредит"),
            ("not-eligible-loan-terms", "Не подхододит по условиям кредитования"),
            ("not-satisfied-service", "Не доволен обслуживанием"),
        ],
        null=True,
        blank=True,
    )

    missed_call = models.CharField(
        max_length=50,
        verbose_name="missed call",
        choices=[
            ("not-available", "Не доступен"),
            ("not-respond", "Не отвечает"),
            ("away-busy", "Нет на месте(занят)"),
            ("someone-else-number", "Чужой номер"),
            ("outside-Republic", "За пределами РТ"),
        ],
        null=True,
        blank=True,
    )

    customer = models.ForeignKey(
        to="customer.Customer", on_delete=models.PROTECT
    )

    active_in_abacus = models.BooleanField("active", default=False)

    def __str__(self):
        return f"{self.id} - {self.application_receipt_channel}"
