from django.urls import path
from registration import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register',views.Inscription,name='compte'),
    path('login',auth_views.LoginView.as_view(template_name='registration/login.html'),name='connexion'),
    path('logout',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
]