from django.shortcuts import render,redirect, get_object_or_404
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
              'posts': posts,
              }
   
   return render(request, 'postroll.html', context)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Upewnij się, że użytkownik jest autorem posta
    if post.author == request.user:
        post.delete()
        return redirect('postroll')  # Przekieruj użytkownika na stronę z postami
    else:
        # Obsłuż przypadki, gdy użytkownik nie jest autorem posta
        # Możesz dodać odpowiedni komunikat lub inne działania
        pass