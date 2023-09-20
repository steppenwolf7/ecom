from django.urls import path, include
from . import views


urlpatterns = [
     path('postroll/', views.postroll, name='postroll'),
     path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
     path('edit_post/<int:post_id>/', views.edit_post, name='edit_post')
    ]