from django import template

register = template.Library()

data = {
  'W': { 'display_en': 'weekly instalments - 7 days', 'display_ru': 'Еженедельные взносы - 7 дней'},
  'F': { 'display_en': 'fortnight instalments-15 days', 'display_ru': 'Взносы двух недель - 15 дней'},
  'M': { 'display_en': 'monthly instalments-30 days', 'display_ru': 'Ежемесячные взносы - 30 дней'},
  'B': { 'display_en': 'bimonthly instalments-60 days', 'display_ru': 'Взносы дважды в месяц - 60 дней'},
  'Q': { 'display_en': 'quarterly instalments-90 days', 'display_ru': 'Квартальные взносы - 90 дней'},
  'T': { 'display_en': 'Trimester four-monthly instalments-120 days', 'display_ru': 'Триместровые четырехмесячные взносы - 120 дней'},
  'C': { 'display_en': 'instalments every five months-150 days', 'display_ru': 'Взносы каждые 5 месяцев - 150 дней'},
  'S': { 'display_en': 'instalments every six months-180 days', 'display_ru': 'Взносы каждые 6 месяцев - 180 дней'},
  'Y': { 'display_en': 'Yearly instalments-360 days', 'display_ru': 'Годовые взносы - 360 дней'},
  'I': { 'display_en': 'irregular instalments', 'display_ru': 'Нерегулярные взносы'},
}

@register.filter
def crif_get_payment_periodicity(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string