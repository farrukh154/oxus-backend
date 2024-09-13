from common.fields import create_char_field
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.AbstractBaseModel import AbstractBaseModel
from division.models.branch.model import Branch
from request_credit.models.r_status.model import RequestStatus
from division.models.currency.model import Currency
from request_credit.models.r_status.model import CREATED_UID
from request_credit.models.r_status.model import APPROVED_UID
from request_credit.models.r_status.model import DENIED_UID
from request_credit.models.r_status.model import POSTPONED_UID
from datetime import datetime
from division.models.district.model import District
from common.mixins import WhoDidItMixin
from django.conf import settings
from common.current_user import get_current_user
from model_utils import FieldTracker
from customer.models.customer.model import Customer
from common.constants import STANDARD_YES_NO_CHOICE, STANDARD_MALE_FEMALE_CHOICE

class RequestCredit(AbstractBaseModel, WhoDidItMixin):
    class Meta:
        verbose_name = _("request credit")
        verbose_name_plural = _("request credits")

    tracker = FieldTracker()

    credit_ID = create_char_field(
        max_length=32, verbose_name=_("credit account"), null=True, blank=True
    )

    status = models.ForeignKey(
        RequestStatus,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='request_credit',
        verbose_name=_("status")
    )
    status_change_date = models.DateTimeField(
        _("status change date"), null=True, blank=True
    )
    status_change_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='request_credit',
        verbose_name=_("status change by")
    )

    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, verbose_name=_("branch"))

    family_number = models.IntegerField(_("family number"),)
    family_number_has_income = models.IntegerField(
        _("family number has income"),
    )
    current_debt = models.CharField(
        max_length=50,
        verbose_name=_("current debt"),
        choices=STANDARD_YES_NO_CHOICE,
    )
    current_debt_name = create_char_field(
        max_length=255, verbose_name=_("current debt name"), null=True, blank=True
    )
    acted = models.CharField(
        max_length=50,
        verbose_name=_("acted"),
        choices=STANDARD_YES_NO_CHOICE,
    )
    full_time_employees = models.IntegerField(
        _("number of full-time employees?"),
    )
    new_job = models.IntegerField(_("creation of new jobs"),)

    information_source = models.CharField(
        max_length=50,
        verbose_name=_("source of information"),
        choices=[
            ("tv", "Реклама дар телевизион"),
            ("radio", "Реклама дар радио"),
            ("newspaper", "Реклама дар рӯзнома"),
            ("internet", "Реклама дар интернет"),
            ("banner", "Баннер/шитҳо"),
            ("oxus", "Корманди Оксус"),
            ("third_person", "Шахси сеюм"),
            ("other", "Дигар"),
        ],
    )

    economic_activity = models.ForeignKey(
        to="request_credit.EconomicActivity",
        on_delete=models.PROTECT,
        verbose_name=_("economic activity"),
    )
    economic_activity_type = models.ForeignKey(
        to="request_credit.EconomicActivityType",
        on_delete=models.PROTECT,
        verbose_name=_("economic activity type"),
    )

    work_experience = models.IntegerField(_("work experience"),)

    request_amount = models.IntegerField(_("request amount"),)

    currency_new = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT,
        verbose_name=_("currency"),
        related_name="currency_new",
    )

    request_installment = models.IntegerField(
        _("request installment"),
    )
    credit_purpose = models.ForeignKey(
        to="request_credit.CreditPurpose",
        on_delete=models.PROTECT,
        verbose_name=_("credit purpose"),
    )
    request_grace_period = models.IntegerField(
        _("request grace period"),
    )
    investment_sector = models.CharField(
        max_length=50,
        verbose_name=_("investment sector"),
        choices=[
            ("trad", "Савдо"),
            ("service", "Хизматрасонӣ"),
            ("production", "Истеҳсолот"),
            ("horticulture", "Растанипарварӣ"),
            ("livestock", "Чорвопарварӣ"),
            ("cons", "Истеъмолӣ"),
        ],
    )

    # самодеклараци
    activity_location = create_char_field(
        max_length=255,
        verbose_name=_("address of location of activity"),
        null=True,
        blank=True,
    )

    education = models.CharField(
        max_length=50,
        verbose_name=_("education"),
        choices=[
            ("university_institute", "Донишгоҳ/Донишкада"),
            ("college_technical_school", "Коллеҷ/Техникум"),
            ("high_school", "Мактаби миёна"),
        ],
        null=True,
        blank=True,
    )

    education_info = create_char_field(
        max_length=255,
        verbose_name=_("education info"),
        null=True,
        blank=True,
    )

    monthly_income = models.IntegerField(_("monthly income"), null=True, blank=True)
    monthly_income_info = create_char_field(
        max_length=255, verbose_name=_("monthly income info"), null=True, blank=True
    )

    monthly_household_expenses = models.IntegerField(
        _("monthly household expenses"), null=True, blank=True
    )
    monthly_household_expenses_info = create_char_field(
        max_length=255,
        verbose_name=_("monthly household expenses info"),
        null=True,
        blank=True,
    )

    monthly_payment_loans = models.IntegerField(
        _("monthly payment loans"), null=True, blank=True
    )
    monthly_payment_loans_info = create_char_field(
        max_length=255,
        verbose_name=_("monthly payment loans info"),
        null=True,
        blank=True,
    )

    monthly_profit_info = create_char_field(
        max_length=255, verbose_name=_("monthly profit info"), null=True, blank=True
    )

    total_business_assets = models.IntegerField(
        _("total business assets"), null=True, blank=True
    )
    total_business_assets_info = create_char_field(
        max_length=255,
        verbose_name=_("total business assets info"),
        null=True,
        blank=True,
    )

    client_capital = models.IntegerField(_("client capital"), null=True, blank=True)
    client_capital_info = create_char_field(
        max_length=255, verbose_name=_("client capital info"), null=True, blank=True
    )

    total_household_assets = models.IntegerField(
        _("total household assets"), null=True, blank=True
    )
    total_household_assets_info = create_char_field(
        max_length=255,
        verbose_name=_("total household assets info"),
        null=True,
        blank=True,
    )

    approve_amount = models.IntegerField(_("approve amount"), null=True, blank=True)

    approve_installment = models.IntegerField(
            _("approve installment"), null=True, blank=True
        )

    approve_currency_new = models.ForeignKey(
        Currency, 
        on_delete=models.PROTECT, 
        verbose_name=_("approve currency"),
        related_name="approve_currency_new",
        null=True,
        blank=True,
    )

    approve_interest = models.DecimalField(
            _("approve interest"), null=True, blank=True, max_digits=12,
        decimal_places=2,
        )

    approve_grace_period = models.IntegerField(
            _("approve grace period"), null=True, blank=True
        )

    approve_issue_fee = models.DecimalField(
            _("approve issue fee"), null=True, blank=True, max_digits=12,
        decimal_places=2,
        )

    credit_product = models.ForeignKey(
        to="credits.CreditProduct",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("credit product"),
    )

    rating_internal = models.CharField(
        max_length=50,
        verbose_name=_("rating internal"),
        choices=STANDARD_YES_NO_CHOICE,
        null=True,
        blank=True,
    )
    rating_external = models.CharField(
        max_length=50,
        verbose_name=_("rating external"),
        choices=STANDARD_YES_NO_CHOICE,
        null=True,
        blank=True,
    )

    approve_condition = models.CharField(
        max_length=50,
        verbose_name=_("approve condition"),
        choices=[
            ("after-current", "Қарз пас аз пардохти қарзи чори дода мешавад"),
            ("account", "Хисоббаробаркунӣ"),
            ("guarantor", "Қарз бо пешниҳоди зомин дода мешавад"),
        ],
        null=True,
        blank=True,
    )

    rejection_reason = models.ForeignKey(
        to="request_credit.RejectionReason",
        related_name="request_rejection",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("rejection reason"),
    )

    client_rejection_reason = models.ForeignKey(
        to="request_credit.RejectionReason",
        related_name="request_client_rejection",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("client rejection reason"),
    )

    postponed_info = create_char_field(
        max_length=255,
        verbose_name=_("postponed info"),
        null=True,
        blank=True,
    )

    decision_client = models.ForeignKey(
        to='request_credit.ClientDecision', on_delete=models.PROTECT, null=True, blank=True, verbose_name=_("decision client"),
    )

    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, verbose_name=_("customer"),
    )

    underwriter_status = models.ForeignKey(
        RequestStatus,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='underwriter_request_credit',
        verbose_name=_("underwriter status"),
    )
    underwriter_status_change_date = models.DateTimeField(
        _("underwriter status change date"), null=True, blank=True
    )
    underwriter_status_change_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='underwriter_request_credit',
        verbose_name=_("underwriter status change by"),
    )

    result = models.CharField(
        max_length=50,
        verbose_name=_("result"),
        choices=[("disbursed", "Выдано"), ("cancelled", "Отказано")],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.id}-{self.customer}"

    def save(self, *args, **kwargs):
        if not self.pk and not self.status:
            self.status = RequestStatus.objects.get(uid=CREATED_UID)
            self.status_change_date = datetime.now()
            self.status_change_by = get_current_user(self)
        if self.tracker.has_changed("status_id") and self.pk:
            self.status_change_date = datetime.now()
            self.status_change_by = get_current_user(self)
            if self.status.uid in [APPROVED_UID, DENIED_UID, POSTPONED_UID]:
                self.underwriter_status = self.status
                self.underwriter_status_change_date = datetime.now()
                self.underwriter_status_change_by = get_current_user(self)

        super().save(*args, **kwargs)
