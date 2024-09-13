from common import serializers
from common.fields import UploadFileField
from common.fields import UploadFileMixin
from django.apps import AppConfig
from django.apps import apps
from model_utils import FieldTracker
from rest_framework.serializers import ModelSerializer


class CommonAppConfig(AppConfig):
    name = 'common'

    def ready(self):
        ModelSerializer.serializer_field_mapping[UploadFileField] = serializers.UploadFileField
        # we use local import here because importing of DynamicREST classes toggles Django auth models,
        # but the auth app is not ready at that moment
        from dynamic_rest.viewsets import DynamicModelViewSet
        from common.metadata.metadata import AdvancedDynamicMetadata

        DynamicModelViewSet.metadata_class = AdvancedDynamicMetadata

        for model in apps.get_models():
            if not hasattr(model, 'tracker') or not isinstance(getattr(model, 'tracker'), FieldTracker):
                for field in model._meta.get_fields():
                    if isinstance(field, UploadFileMixin):
                        raise NotImplementedError(
                            f'Model {model} must have a "tracker" field from "model_utils.FieldTracker",'
                            f' because it has a "UploadFile..." field and him needed it!'
                            f' Sorry for this exception, just add "tracker = FieldTracker()" to {model}.'
                        )
