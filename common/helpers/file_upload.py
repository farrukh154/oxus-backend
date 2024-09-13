import json
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

REQUEST_FILE_KEY = 'files'
RESPONSE_FILE_KEY = 'file_paths'

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def file_upload_endpoint(request):
    local_file_storage = FileSystemStorage()
    """ returns filepaths whose beginning from the directory named "upload" which placed in MEDIA_ROOT """
    file_paths, response = [], {}
    files = request.FILES.getlist(REQUEST_FILE_KEY, None)
    if not files:
        if REQUEST_FILE_KEY in request.POST:
            error_message = _('There are not any files in the request!')
        else:
            error_message = ' '.join([_('There is not a key in the request:'), REQUEST_FILE_KEY])
        return HttpResponse(content=error_message, status=HTTP_400_BAD_REQUEST)
    for file in files:
        file_paths.append(
            local_file_storage.save(os.path.join(settings.FILE_UPLOAD_DIR, file.name), file)
        )
    response[RESPONSE_FILE_KEY] = file_paths
    return HttpResponse(content=json.dumps(response), status=HTTP_200_OK)
