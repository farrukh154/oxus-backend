from oxus.utils.try_get_attr import try_get_attr
from users.models import User

ATTR_CURRENT_USER = '_current_user'


def set_current_user(model_instance, user: User) -> User:
    setattr(model_instance, ATTR_CURRENT_USER, user)


def get_current_user(model_instance) -> User:
    return try_get_attr(lambda: getattr(model_instance, ATTR_CURRENT_USER))
