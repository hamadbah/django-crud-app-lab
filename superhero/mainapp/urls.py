from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('superhero/', views.hero_index, name='index'),
    path('superhero/<int:hero_id>/', views.hero_detail, name='detail'),
    path('superhero/create', views.HeroCreate.as_view(), name='hero_create'),
    path('superhero/<int:pk>/update/', views.HeroUpdate.as_view(), name='hero_update'),
    path('superhero/<int:pk>/delete/', views.HeroDelete.as_view(), name='hero_delete'),
    path('superhero/<int:hero_id>/add_weapon/', views.add_weapon, name='add_weapon')
]