#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django_registration.views import RegistrationView
from index.forms import CustomUserForm
#from index.models import CustomUser
from django.contrib.auth import login  
#from django.contrib import messages
from postroll.models import Post

"""
def register(request):
   if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
      messages.success(request, "Your accout is created!")   
      return redirect('index')
   else:
      form = UserCreationForm(request.POST)
   return render(request, 'register.html', {'form':form})"""

class MyRegistrationView(RegistrationView):
   form_class=CustomUserForm
   success_url='/'
   
   
   def register(self, form):
      user = form.save(commit=False) # definiuje obiekt user i wstrzymuje jego zapis
      
      if 'image' in self.request.FILES:
            user.image = self.request.FILES['image']  # Przypisuje przesłane zdjęcie do pola image

      user.save()
      login(self.request, user)
   
      return user
   
   


#@login_required
def index(request):                                             
   posts = Post.objects.all() 
   username = request.user.username
   
   context = {'username': username,
              'posts': posts}
   return render(request, 'index.html', context)

class MyLogOutView(LogoutView):
   template_name = 'registration/logout.html'
   #next_page = 'accounts/logout'   
   pass

class MyLoginView(LoginView):
   next_page = "index"
   pass


   
   
  