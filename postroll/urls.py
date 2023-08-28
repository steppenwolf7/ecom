from django.urls import path, include
from . import views


urlpatterns = [
     path('postroll/', views.postroll, name='postroll'),
    ]