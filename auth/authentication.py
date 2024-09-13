from common.middleware.WhoDidItMiddleware import mark_who_did_it
from django.db.models import signals
from functools import partial as curry
from rest_framework_simplejwt.authentication import JWTAuthentication as RawJWTAuthentication


class JWTAuthentication(RawJWTAuthentication):
    DISPATCH_UID: str = 'mark_who_did_it'

    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is not None:
            user, auth = user_auth_tuple

            # process mark_who_did_it feature
            signals.pre_save.disconnect(dispatch_uid=self.DISPATCH_UID)
            mark_who_did_curried = curry(mark_who_did_it, user)
            signals.pre_save.connect(mark_who_did_curried, dispatch_uid=self.DISPATCH_UID)
            # we don't want our receiver function to be garbage collected after we exit this function, so sticking it to
            # request, thus it would be removed with it
            request._mark_who_did_curried = mark_who_did_curried

        return user_auth_tuple
