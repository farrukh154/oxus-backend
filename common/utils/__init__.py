from os import mkdir
from os.path import exists
from os.path import isdir
from os.path import sep as os_path_sep
from rest_framework.exceptions import PermissionDenied

def get_model_meta(view):
    return view.serializer_class.Meta.model._meta

def create_dir_by_path(path):
    dirs = path.split(os_path_sep)
    curr_path = ''
    for d in dirs:
        curr_path = curr_path + d
        if not exists(curr_path):
            mkdir(curr_path)
        else:
            if not isdir(curr_path):
                raise CreateDirectoryForScansError('Cannot create directory for scans.')
        curr_path += os_path_sep

class CreateDirectoryForScansError(Exception):
    def __init__(self, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = "Error on processing with path"
        super().__init__(msg)


def has_permission(user, model, permission):
    return user.has_perm(f'{model._meta.app_label}.{permission}')


def check_permission(user, model, permission, message=None):
    if not has_permission(user, model, permission):
        raise PermissionDenied(message)