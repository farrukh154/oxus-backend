from common.utils.i18n.lang_switcher import switch_lang_code
from django.urls import path, include
# from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('division/', include('division.urls')),
    path('request_credit/', include('request_credit.urls')),
    path('change_lang/<str:lang>', switch_lang_code, name='change_lang'),
    path('accounting/', include('accounting.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [path('admin/rosetta/', include('rosetta.urls'))]