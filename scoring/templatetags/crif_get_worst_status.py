from django import template

register = template.Library()

data = {
  'U': { 'display_en': 'Previous delinquency rectified', 'display_ru': 'Предыдущая просрочка погашена'},
  'W': { 'display_en': 'Credit line taken on from another debtor', 'display_ru': 'Кредитная линия, взятая у другого должника'},
  'A': { 'display_en': 'There are unpaid installments, advance amount being paid', 'display_ru': 'Есть неоплаченные взносы, дополнительная сумма заплачена'},
  'I': { 'display_en': 'Under dispute / non performing', 'display_ru': 'Спорное положение/невыполнение'},
  'H': { 'display_en': 'Court injunction', 'display_ru': 'Судебный запрет'},
  'G': { 'display_en': 'Foreclosure underway', 'display_ru': 'Лишение прав выкупа закладной в стадии реализации'},
  'F': { 'display_en': 'Bankruptcy request', 'display_ru': 'Запрос банкротства'},

  'V': { 'display_en': 'Voluntary abandonment, renewal missing', 'display_ru': 'Добровольный отказ, возобновление отсутствует'},
  'T': { 'display_en': 'Dispute', 'display_ru': 'Спорное положение'},
  'B': { 'display_en': 'Blocked (credit relationship suspended)', 'display_ru': 'Заблокировано (приостановленные кредитные отношения)'},
  'R': { 'display_en': 'Revocation due to arrears', 'display_ru': 'Аннулирование из-за задолженности'},
  'P': { 'display_en': 'Write-off (BLW)', 'display_ru': 'Списание со счета (BLW)'},
  'S': { 'display_en': 'Under litigation / Delinquent', 'display_ru': 'Под тяжбой / Преступление'},
  'C': { 'display_en': 'Credit transferred for collection', 'display_ru': 'Кредит перешел во взыскание'},
}

@register.filter
def crif_get_worst_status(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string