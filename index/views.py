from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
   if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
      messages.success(request, "Your accout is created!")   
      return redirect('index')
   else:
      form = UserCreationForm(request.POST)
   return render(request, 'register.html', {'form':form})

#@login_required
def index(request):                                             
   username = request.user.username
   context = {'username': username}
   return render(request, 'index.html', context)

class MyLogOutView(LogoutView):
   template_name = 'registration/logout.html'
   #next_page = 'accounts/logout'   
   pass

class MyLoginView(LoginView):
   next_page = "index"
   pass


   
   
  