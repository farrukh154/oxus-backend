from django.http import HttpResponseRedirect
from django.utils import translation


def switch_lang_code(request, lang):
    translation.activate(lang)
    request.session['language'] = lang
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
