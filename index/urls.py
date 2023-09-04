#from django_registration.backends.one_step.views import RegistrationView
#from index.forms import CustomUserForm
from . import views
from .views import MyLogOutView, MyLoginView
from django.urls import path, include
from .views import MyRegistrationView 


urlpatterns = [
    path('accounts/logout/', MyLogOutView.as_view(), name='my-logout'),
    path('accounts/login/', MyLoginView.as_view(), name='my-login'),
    #path('accounts/register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('accounts/register/', MyRegistrationView.as_view(),name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path("accounts/", include("django.contrib.auth.urls"))
    
    

]