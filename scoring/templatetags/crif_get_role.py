from django import template

register = template.Library()

data = {
  'A': {'display_en': 'Borrower', 'display_ru': 'Заёмщик'},
  'C': {'display_en': 'Co-Borrower', 'display_ru': 'Созаёмщик'},
  'G': {'display_en': 'Guarantor', 'display_ru': 'Поручитель'},
}

@register.filter
def crif_get_role(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string