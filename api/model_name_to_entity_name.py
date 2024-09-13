from typing import Optional

from dynamic_rest import routers

from common.utils import get_model_meta


def _form_key(app, model):
    return f'{app}.{model}'


def _build_model_name_to_entity_name_map():
    result = {}
    for app, views in routers.directory.items():
        for entity_name, info in views.items():
            model_meta = get_model_meta(info['_viewset'])
            result[_form_key(model_meta.app_label, model_meta.model_name)] = entity_name
    return result


_model_name_to_entity_name_map = None


def get_entity_name(app: str, model_name: str) -> Optional[str]:
    global _model_name_to_entity_name_map
    if _model_name_to_entity_name_map is None:
        _model_name_to_entity_name_map = _build_model_name_to_entity_name_map()
    return _model_name_to_entity_name_map.get(_form_key(app, model_name))
