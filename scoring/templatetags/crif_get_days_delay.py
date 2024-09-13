from django import template

register = template.Library()

data = {
  '0': { 'display_en': 'Pay as agreed', 'display_ru': 'Плата по согласованию'},
  'A': { 'display_en': '1-29 days delay', 'display_ru': 'Задержка 1-29 дней'},
  '1': { 'display_en': '30-59 days delay', 'display_ru': 'Задержка 30-59 дней'},
  '2': { 'display_en': '60-89 days delay', 'display_ru': 'Задержка 60-89 дней'},
  '3': { 'display_en': '90-119 days delay', 'display_ru': 'Задержка 90-119 дней'},
  '4': { 'display_en': '120-149 days delay', 'display_ru': 'Задержка 120-149 дней'},
  '5': { 'display_en': '150-179 days delay', 'display_ru': 'Задержка 150-179 дней'},
  '6': { 'display_en': 'More than 180 days delay', 'display_ru': 'Более 180 дней задержки'},
}

@register.filter
def crif_get_days_delay(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string