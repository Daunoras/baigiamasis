from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    path('plants/', include('plantwatering.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='plants/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
