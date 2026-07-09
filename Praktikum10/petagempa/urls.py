from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='petagempa_home'),
    path('home/', views.home, name='petagempa_home_page'),
    path('berita/', views.berita, name='petagempa_berita'),
]
