from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render
#import requests

@login_required
def index(request):                                             
   username = request.user.username
   context = {'username': username}
   return render(request, 'index.html', context)
   
   
   """ username = request.POST["username"]  # to jest formularz
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    #context = {'username':username}
    
    if user is not None:
        login(request, user)
        render(request, 'login.html', context=context)
    else:
        render(request, 'index.html', context=context)
        """
   