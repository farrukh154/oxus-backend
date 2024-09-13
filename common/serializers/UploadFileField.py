from rest_framework.fields import FileField


class UploadFileField(FileField):
    """
    Serializer for our pre-uploaded file fields

    The incoming data is a string, the outgoing data is url as in FileField
    """

    def to_internal_value(self, data):
        # we await a string as the incoming data
        return str(data)
