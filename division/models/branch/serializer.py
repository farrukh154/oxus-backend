from dynamic_rest.serializers import DynamicModelSerializer

from .model import Branch


class BranchSerializer(DynamicModelSerializer):
    class Meta:
        name = 'branch'
        model = Branch
        fields = (
            'id', 'name', 'description', 'code', 'regional_branch', 'active', 'abacus_id'
        )
