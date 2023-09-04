from django.contrib import admin
from .models import CustomUser  

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'has_profile_image')
    def has_profile_image(self, obj):
        if obj.image:
            return 'Yes'  # Użytkownik ma zdjęcie profilowe
        return 'No'  # Użytkownik nie ma zdjęcia profilowego

    has_profile_image.short_description = 'Has Profile Image'      