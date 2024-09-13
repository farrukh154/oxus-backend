from api.router import router
from django.urls import include
from django.urls import path

urlpatterns = [
    path('', include(router.urls)),
]