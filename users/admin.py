from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User
from django.contrib import admin
from oxus.utils.try_get_attr import try_get_attr

class UserAdmin(DjangoUserAdmin):
    model = User
    fieldsets = DjangoUserAdmin.fieldsets + (
        (
            'Custom fields',
            {
                'fields': (
                    'is_swift_loan_user',
                    'swift_loan_role',
                    'branches',
                    'description',
                    'user_signature',
                ),
            },
        ),
    )
    list_display = (
        'id',
        'email',
        'username',
        'get_full_name',
        'is_active',
        'is_superuser',
        'is_swift_loan_user',
        'swift_loan_role',
        'get_branches',
        'description',
    )
    list_filter = (
        'is_active',
        'swift_loan_role',
        'branches',
    )

    def get_branches(self, obj):
        branches = try_get_attr(lambda: obj.branches.all())

        return (
            ', '.join(b.name for b in branches)
            if obj.branches and obj.branches.exists()
            else '-'
        )

admin.site.register(User, UserAdmin)