from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sports/', views.sports, name='sports'),
    path('science/', views.science, name='science'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('technology/', views.technology, name='technology'),
]
