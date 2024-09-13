from django.contrib.auth.models import AbstractUser
from django.db import models
from common.fields import create_char_field
from os.path import sep as os_path_sep
from common.utils import create_dir_by_path
from datetime import datetime
from model_utils import FieldTracker
from django.utils.translation import gettext_lazy as _

def get_signature_scan_path(instance, filename):
    path_to_docs = os_path_sep.join(['user_signature'])
    create_dir_by_path(path_to_docs)
    return os_path_sep.join([path_to_docs, f"{datetime.today().strftime('%Y-%m-%d-%H%M%S')}_{filename}"])

SWIFT_LOAN_ROLE = (
    ('non-swift-loan', 'Пользователь не связан с Swift Loan'),

    ('customer-service-specialist', 'Специалиста по обслуживанию клиентов'),
    ('call-officer', 'Агент колл-центра'),
    ('operation-officer', 'Операционный офицер'),
    ('manager', 'ДФ/РЦМО'),
    ('cashier', 'Кассир'),
    ('underwriter', 'Андеррайтер'),
    ('underwriter-manager', 'Руководитель отдела Андеррайтинга'),
)
class User(AbstractUser):
  class Meta:
    db_table = 'auth_user'

    permissions = (
      ('view-helpdesk-menu-item_user', 'Can view helpdesk menu item'),
      ('view-blacklist-menu-item_user', 'Can view blacklist menu item'),
      ('view-report-menu-item_user', 'Can view report menu item'),
      ('view-terminal-menu-item_user', 'Can view terminal menu item'),
      ('view-crif-menu-item_user', 'Can view crif menu item'),
      ('view-settings-menu-item_user', 'Can view settings menu item'),
      ('view-exchange-rate-tab-item_user', 'Can view exchange rate tab item'),
      ('view-document-menu-item_user', 'Can view document menu item'),
      ('view-loan-application-menu-item_user', 'Can view loan application menu item'),
      ('view-customer-menu-item_user', 'Can view customer menu item'),
      ('view-call-menu-item_user', 'Can view call menu item'),
      ('view-abacus-document-tab-item_user', 'Can view abacus document tab item'),
    )

  is_swift_loan_user = models.BooleanField('Пользователь Swift loan', default=False)

  swift_loan_role = models.CharField(
      max_length=50,
      verbose_name='smart loan role',
      choices=SWIFT_LOAN_ROLE,
      default=SWIFT_LOAN_ROLE[0][0],
  )

  branches = models.ManyToManyField(
      verbose_name='branches',
      to='division.Branch',
      blank=True,
      related_name='purchases_reports',
  )

  description = create_char_field(
      max_length=255,
      verbose_name='description',
  )

  user_signature = models.FileField(
    verbose_name="User scan signature",
    upload_to=get_signature_scan_path,
    null=True,
    blank=True
  )

  get_full_name = models.CharField(
      max_length=255,
      verbose_name=_('full name'),
      blank=True
    )
  
  tracker = FieldTracker()
  
  def __str__(self):
        return f'{self.get_full_name}'

  def save(self, *args, **kwargs):
        if self.tracker.has_changed('first_name') or self.tracker.has_changed('last_name'):
            self.get_full_name = f'{self.last_name} {self.first_name}'
        super().save(*args, **kwargs)