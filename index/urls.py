from django.urls import path, include
from . import views
from .views import MyLogOutView, MyLoginView

urlpatterns = [
    path('accounts/logout/', MyLogOutView.as_view(), name='my-logout'),
    path('accounts/login/', MyLoginView.as_view(), name='my-login'),
    path('', views.index, name='index'),
    path("accounts/", include("django.contrib.auth.urls"))
]