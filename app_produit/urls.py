from django.urls import path
from app_produit import views


urlpatterns = [
    path('',views.accueil,name='accueil'),
]