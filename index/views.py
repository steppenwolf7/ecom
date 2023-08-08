#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.shortcuts import redirect


class MyLogOutView(LogoutView):
   template_name = 'registration/logout.html'
   #next_page = 'accounts/logout'   
   pass

class MyLoginView(LoginView):
   next_page = "index"
   pass


@login_required
def index(request):                                             
   username = request.user.username
   context = {'username': username}
   return render(request, 'index.html', context)
   
   
  