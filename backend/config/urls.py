from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/automations/", include("automations.urls")),
    path("api/auth/", include("accounts.urls")),
]
