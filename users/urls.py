from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="signup"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/<pk>', views.ProfileUpdateView.as_view(), name="profile"),
]
