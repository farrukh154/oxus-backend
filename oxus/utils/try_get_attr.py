from typing import Callable, Any

from django.core.exceptions import ObjectDoesNotExist


def try_get_attr(f: Callable, default: Any = None) -> Any:
    try:
        return f()
    except (AttributeError, ObjectDoesNotExist):
        return default
