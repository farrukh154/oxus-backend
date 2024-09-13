from django.db.models import signals
from django.utils.deprecation import MiddlewareMixin
from functools import partial as curry


def mark_who_did_it(user, sender, instance, **kwargs):
    if user is None:
        return  # no user - no preset
    field_names = [f.name for f in instance._meta.fields]
    if 'created_by' in field_names and not instance.pk:
        instance.created_by = user
    if 'updated_by' in field_names:
        instance.updated_by = user


class WhoDidItMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # if not request.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
        if hasattr(request, 'user') and request.user.is_authenticated:
            user = request.user
        else:
            user = None

        mark_whodid_curried = curry(mark_who_did_it, user)
        signals.pre_save.connect(mark_whodid_curried,  dispatch_uid=(self.__class__, request,), weak=False)

    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid=(self.__class__, request,))
        return response
