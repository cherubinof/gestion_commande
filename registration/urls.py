from django.urls import path
from registration import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=LoginForm),name='connexion'),
    path('logout',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
]