from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class LocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            lang = (
                request.session['language'] if request.session.get('language') else 'en'
            )
            translation.activate(lang)
            request.LANGUAGE_CODE = lang

    def process_response(self, request, response):
        translation.deactivate()
        return response
