from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def postroll(request):                                             
   username = request.user.username
   context = {'username': username}
   return render(request, 'postroll.html', context)
