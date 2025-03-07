"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

favicon_view = RedirectView.as_view(
    url="/static/assets/imgs/favicon.ico", permanent=True
)

urlpatterns = (
    [
        path("favicon.ico", favicon_view),
        path("", views.LandingPageView.as_view(), name="home"),
        path("", include("pwa.urls")),  # django-pwa manifest/serviceworker urls
        path("accounts/", include("accounts.urls", namespace="accounts")),
        path("poisons/", include("poisons.urls", namespace="poisons")),
        path("admin/", admin.site.urls),
        path("api-auth/", include("rest_framework.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


# Admin Page Configs
admin.site.site_header = "PoisonWiki"
admin.site.site_title = "CIRC"
admin.site.index_title = None
