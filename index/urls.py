from django.urls import path, include
from . import views
from .views import MyLogOutView, MyLoginView
from django_registration.backends.activation.views import RegistrationView

from index.forms import CustomUserForm


urlpatterns = [
    path('accounts/logout/', MyLogOutView.as_view(), name='my-logout'),
    path('accounts/login/', MyLoginView.as_view(), name='my-login'),
    #path('accounts/register/', views.register, name='register'),
    path('', views.index, name='index'),
    
    
    path('accounts/register/', RegistrationView.as_view(form_class=CustomUserForm),name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path("accounts/", include("django.contrib.auth.urls"))

]