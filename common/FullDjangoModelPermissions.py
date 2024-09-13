from rest_framework.permissions import DjangoModelPermissions

class FullDjangoModelPermissions(DjangoModelPermissions):
    perms_map = dict(DjangoModelPermissions.perms_map)
    perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']