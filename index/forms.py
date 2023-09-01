#from django import forms

from django_registration.forms import RegistrationForm

from index.models import CustomUser


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser