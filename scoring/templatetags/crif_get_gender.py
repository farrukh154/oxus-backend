from django import template

register = template.Library()

data = {
  'M': {'display_en': 'Male', 'display_ru': 'Мужской'},
  'F': {'display_en': 'Female', 'display_ru': 'Женский'},
}

@register.filter
def crif_get_gender(string):
  if not string:
    return '-'
  if string in data:
    return data[string]['display_ru']
  return string