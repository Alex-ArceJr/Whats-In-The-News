from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sports/', views.sports, name='sports'),
    path('science/', views.science, name='science'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('technology/', views.technology, name='technology'),
    path('accounts/signup/', views.signup, name='signup'),
    path('technology/<int:article_id>/',
         views.technology_article_detail, name='detail'),
    path('science/<int:article_id>/',
         views.science_article_detail, name='science_detail'),
    path('sports/<int:article_id>/',
         views.sports_article_detail, name='sports_detail'),
    path('entertainment/<int:article_id>/',
         views.entertainment_article_detail, name='entertainment_detail'),

]
