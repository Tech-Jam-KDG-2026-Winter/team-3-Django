from django.contrib import admin
from django.urls import path, include
from apps.common.api.health import healthz

urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthz/", healthz),
    path("test/", include("testapp.urls")),
    path(
        "",
        include(("accounts.urls", "accounts"), namespace="accounts"),
    ),
]
