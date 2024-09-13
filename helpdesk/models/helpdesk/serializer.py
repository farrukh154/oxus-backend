from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField
from .model import Helpdesk


class HelpdeskSerializer(DynamicModelSerializer):
    status = DynamicRelationField(
        'helpdesk.models.helpdesk_status.serializer.HelpdeskStatusSerializer',
        label='status',
    )

    priority = DynamicRelationField(
        'helpdesk.models.helpdesk_priority.serializer.HelpdeskPrioritySerializer',
        label='priority',
    )

    branch = DynamicRelationField(
        'division.models.branch.serializer.BranchSerializer',
        label ='branch',
    )

    for_whom = DynamicRelationField(
        "users.serializer.UserSerializer",
        label="for whom",
    )

    created_by = DynamicRelationField(
        "users.serializer.UserSerializer",
        label="Created by",
        read_only=True,
    )

    updated_by = DynamicRelationField(
        "users.serializer.UserSerializer",
        label="Updated by",
        read_only=True,
    )


    class Meta:
        name = 'helpdesk'
        model = Helpdesk
        fields = (
            'id',
            'name',
            'status',
            'priority',
            'branch',
            'created',
            'updated',
            'created_by',
            'updated_by',
            'for_whom',
            'description'
        )



