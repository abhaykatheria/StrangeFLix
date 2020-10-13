from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [

    path('', include("screens.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)