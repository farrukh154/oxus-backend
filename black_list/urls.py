from django.urls import path
from black_list.views import BlackListView

urlpatterns = [
    path('search_person/', BlackListView.as_view(), name='search_person'),
]
