from os.path import sep as os_path_sep
from common.utils import create_dir_by_path
from django.conf import settings
from datetime import datetime
import pypyodbc as odbc
from common.abacus.connection import connection_string

from division.models.branch import Branch
from division.models.currency import Currency
from ..models import Report
from ..models import ReportHistory

def get_uniq_report_name(report_name):
  return f"{report_name}_{datetime.today().strftime('%Y-%m-%d-%H%M%S')}.xlsx"

def get_filename_with_path(report_name):
  path_to_docs = os_path_sep.join([settings.MEDIA_ROOT, settings.GENERATED_REPORTS_DIR])
  # create_dir_by_path(path_to_docs)
  return os_path_sep.join([path_to_docs, report_name])


def get_abacus_branches(branches):
  branch_ids = [
    int(branch_id) for branch_id in branches.split(",") if branch_id.isdigit()
  ]
  branch_abacus_ids = Branch.objects.filter(id__in=branch_ids).values_list('abacus_id', flat=True)
  branch_names = Branch.objects.filter(id__in=branch_ids).values_list('name', flat=True)
  return [','.join(str(x) for x in branch_abacus_ids), ', '.join(str(x) for x in branch_names)]

def get_abacus_currencies(currencies):
  currency_ids = [
      int(currency_id) for currency_id in currencies.split(",") if currency_id.isdigit()
  ]
  currency_abacus_ids = Currency.objects.filter(id__in=currency_ids).values_list('abacus_id', flat=True)
  currency_names = Currency.objects.filter(id__in=currency_ids).values_list('name', flat=True)
  return [','.join(str(x) for x in currency_abacus_ids), ', '.join(str(x) for x in currency_names)]

def create_or_alter_report_function(report_name):
  path_to_sql = f"{settings.BASE_DIR}/reports/report_generate/{report_name}.sql"

  conn = odbc.connect(connection_string)
  cursor = conn.cursor()

  sql_query = ''
  with open(path_to_sql, 'r', encoding="utf8") as inserts:
      for line in inserts:
          if line == 'GO\n':
              cursor.execute(sql_query)
              conn.commit()
              sql_query = ''
          else:
              sql_query = sql_query + line
  inserts.close()

  cursor.close()
  conn.close()

def set_report_header(workbook, writer, report_name, report_version):
  worksheet = writer.sheets[report_name]

  format_subtitle = workbook.add_format({'font_size': 9})

  worksheet.write('D1', 'Report:', format_subtitle)
  format_title = workbook.add_format({'bold': True, 'font_size': 14})
  worksheet.write('D2', report_name.replace('_', ' ').title(), format_title)

  worksheet.write('I1', 'Version:', format_subtitle)
  worksheet.write('I2', report_version)

  worksheet.write('K1', 'Executed time:', format_subtitle)
  format_date = workbook.add_format({'num_format': 'd.mm.yyyy'})
  worksheet.write('K2', datetime.now(), format_date)

  worksheet.write('D4', 'Filters:', format_subtitle)

  img_url = os_path_sep.join([settings.STATIC_ROOT, 'logo.png'])
  worksheet.insert_image('A1', img_url)
  worksheet.freeze_panes(8, 0)

  return worksheet

def create_report_history(report_uid, duration, request, report_name):
  ReportHistory.objects.create(
    duration=duration,
    report=Report.objects.get(uid=report_uid),
    info=request.body.decode("utf-8"),
    xlsx_report=os_path_sep.join([settings.GENERATED_REPORTS_DIR, report_name]),
    generated_by=request.user,
  )