from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

@login_required
def postroll(request):                                             
   if request.method == 'POST':
        form = PostForm(request.POST) #przekazuje formularz do zmiennej
        if form.is_valid():
            # Jeśli formularz jest prawidłowy, zapisz post do bazy danych
            post = form.save(commit=False) 
            post.author = request.user  # Przypisz autora do zalogowanego użytkownika
            post.save()
            return redirect(request.get_full_path()) 
   else:
        form = PostForm() #zapisuje pusty
   
   posts = Post.objects.all() 
   username = request.user.username
   
   context = {'username': username,
              'form': form,
              'posts': posts}
   
   return render(request, 'postroll.html', context)
