from django.shortcuts import render

#@login_required
def postroll(request):                                             
   username = request.user.username
   context = {'username': username}
   return render(request, 'postroll.html', context)
