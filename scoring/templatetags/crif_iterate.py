from django import template

register = template.Library()

data = {
  'M': {'display_en': 'Male', 'display_ru': 'Мужской'},
  'F': {'display_en': 'Female', 'display_ru': 'Женский'},
}

@register.filter
def crif_iterate(object):
  if type(object) == dict:
    return [object]
  return object