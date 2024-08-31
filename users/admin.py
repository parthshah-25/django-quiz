from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_teacher', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {
            "fields": (
                'first_name',
                'last_name',
                'email',
                'password',
                'is_teacher',
                'phone_number',
                'user_image',

            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_teacher'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
