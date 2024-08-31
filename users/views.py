from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404

# Create your views here.


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("login")


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/profile_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.pk != self.request.user.pk:
            raise Http404('Unauthorized!!')
        return obj

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.object.id})


class CustomLogoutView(LogoutView):
    template_name = "users/logout.html"
