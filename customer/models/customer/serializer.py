from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.serializers import DynamicRelationField

from .model import Customer


class CustomerSerializer(DynamicModelSerializer):
    branch = DynamicRelationField(
        "division.models.branch.serializer.BranchSerializer",
        label="branch",
    )
    registration_address = DynamicRelationField(
        "division.models.district.serializer.DistrictSerializer",
        label="registration_address",
    )
    address = DynamicRelationField(
        "division.models.district.serializer.DistrictSerializer",
        label="address",
    )
    class Meta:
        name="customer"
        model = Customer
        fields = (
        'id',
        'name',
        'birthday',
        'gender',
        'client_ID',
        'INN',
        'passport',
        'passport_date',
        'passport_details',
        'branch',
        'registration_address',
        'registration_address_street',
        'address',
        'address_street',
        'phone1',
        'phone2',
        'phone3',
        'family_status',
        'spouse',
        'spouse_phone'
        )
