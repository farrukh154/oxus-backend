from dynamic_rest.viewsets import DynamicModelViewSet
from division.models.branch import Branch
from division.models.branch.serializer import BranchSerializer
from common.FullDjangoModelPermissions import FullDjangoModelPermissions

class BranchViewSet(DynamicModelViewSet):
    queryset = Branch.objects.all()
    permission_classes = (FullDjangoModelPermissions,)
    serializer_class = BranchSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Branch.objects.all()
        else:
            branch_id = user.branches.all().values_list('id', flat=True)
            return Branch.objects.filter(id__in=branch_id)