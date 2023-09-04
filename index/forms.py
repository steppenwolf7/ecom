from django import forms
from django_registration.forms import RegistrationForm
from index.models import CustomUser


class CustomUserForm(RegistrationForm):
    image = forms.ImageField()
    class Meta(RegistrationForm.Meta):  # pozwala wykorzystać model CustomUser zamiast domyślengo User
       model = CustomUser
        