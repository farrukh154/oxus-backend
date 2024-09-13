from django import template

register = template.Library()

@register.filter
def crif_format_date(string):
  if not string:
    return '-'
  return f"{string[:2]}.{string[2:4]}.{string[4:]}"