from django.contrib.admin import ModelAdmin

from .model import Branch


class BranchAdmin(ModelAdmin):
    model = Branch
    change_list_template = "branch_sync_abacus.html"
    readonly_fields = ['abacus_id']
    list_display = (
        'id',
        'name',
        'description',
        'code',
        'regional_branch',
        'active',
        'abacus_id',
    )
    search_fields = ('name',)
