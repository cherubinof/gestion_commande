from django.urls import path
from app_produit import views


urlpatterns = [
    path('',views.accueil,name='accueil'),
    path('list_produit',views.list_produit,name='list-produit'),
    path('ajout_produit',views.ajout_produit,name='ajout-produit'),
    
]