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
    path('superhero/<int:hero_id>/add_weapon/', views.add_weapon, name='add_weapon'),
    path('enemies/', views.EnemyList.as_view(), name='enemies_index'),
    path('enemies/<int:pk>/', views.EnemyDetail.as_view(), name='enemies_detail'),
    path('enemies/create/', views.EnemyCreate.as_view(), name='enemies_create'),
    path('enemies/<int:pk>/update/', views.EnemyUpdate.as_view(), name='enemies_update'),
    path('enemies/<int:pk>/delete/', views.EnemyDelete.as_view(), name='enemies_delete'),
    
    #Associate and Un Associate a toy with a cat this is for many to many relationship
    path('superhero/<int:hero_id>/assoc_enemy/<int:enemy_id>/',views.assoc_enemy, name='assoc_enemy'),
    path('superhero/<int:hero_id>/unassoc_enemy/<int:enemy_id>/',views.unassoc_enemy, name='unassoc_enemy'),
]