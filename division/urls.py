from django.urls import path
from division.utils.sync_address_list import sync_address_list
from division.utils.sync_branch_list import sync_branch_list

urlpatterns = [
    path('sync-address-list/', sync_address_list, name='sync_address_list'),
    path('sync-branch-list/', sync_branch_list, name='sync_branch_list'),
]
