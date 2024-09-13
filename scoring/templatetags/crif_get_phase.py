from django import template

register = template.Library()

data = {
  'RQ': {'display_en': 'Requested', 'display_ru': 'Запрошен'},
  'RN': {'display_en': 'Renounced', 'display_ru': 'Отозван'},
  'RF': {'display_en': 'Refused', 'display_ru': 'Отказан'},
  'LV': {'display_en': 'Living', 'display_ru': 'Существующий'},
  'TM': {'display_en': 'Terminated', 'display_ru': 'Завершен'},
  'TA': {'display_en': 'Terminated in advance', 'display_ru': 'Заранее завершен'},
}
@register.filter
def crif_get_phase(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string