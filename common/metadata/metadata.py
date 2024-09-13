from django.contrib.contenttypes.models import ContentType
from dynamic_rest.metadata import DynamicMetadata
from rest_framework.fields import DecimalField

# from common.serializers import DateTimeWithoutTZFieldSerializer
# from common.serializers import DirectUploadFileField
# from common.serializers import RecTimeIntervalFieldSerializer
from common.utils import get_model_meta


def complete_decimal_fields_info(fields: dict, fields_metadata: dict):
    for field_name, field in fields.items():
        if isinstance(field, DecimalField):
            fields_metadata[field_name]['decimal_places'] = field.decimal_places


# def complete_direct_upload_file_fields_info(fields: dict, fields_metadata: dict):
#     for field_name, field in fields.items():
#         if isinstance(field, DirectUploadFileField):
#             fields_metadata[field_name]['upload_to'] = field.upload_to


class AdvancedDynamicMetadata(DynamicMetadata):
    def determine_metadata(self, request, view):
        # add direct upload field type to "label_lookup"
        # self.label_lookup[DirectUploadFileField] = 'file direct upload'
        # self.label_lookup[DateTimeWithoutTZFieldSerializer] = 'datetime without tz'
        # self.label_lookup[RecTimeIntervalFieldSerializer] = 'rec_time_interval'

        metadata = super().determine_metadata(request, view)
        model_meta = get_model_meta(view)
        metadata['verbose_name'] = model_meta.verbose_name
        metadata['verbose_name_plural'] = model_meta.verbose_name_plural
        metadata['content_type_id'] = ContentType.objects.get_for_model(
            view.serializer_class.Meta.model, for_concrete_model=False,
        ).pk
        complete_decimal_fields_info(view.get_serializer().fields, metadata['properties'])
        # complete_direct_upload_file_fields_info(view.get_serializer().fields, metadata['properties'])
        return metadata
