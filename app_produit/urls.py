from django.urls import path
from app_produit import views


urlpatterns = [
    path('accueil',views.accueil,name='accueil'),
    path('list_produit',views.list_produit,name='list-produit'),
    path('ajout_produit',views.ajout_produit,name='ajout-produit'),
    path('modifier_produit/<int:pk>',views.modifier_produit,name='modifier-produit'),
    path('supprimer_produi/<int:pk>',views.supprimer_produit,name='supprimer-produit'),
    
]