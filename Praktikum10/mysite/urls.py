from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("beranda.urls")),
    path("beranda/", include("beranda.urls")),
    path("petagempa/", include("petagempa.urls")),
    path("admin/", admin.site.urls),
]
