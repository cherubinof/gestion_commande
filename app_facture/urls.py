from django.urls import path
from app_facture import views


urlpatterns = [
    path('facture',views.facture,name='facture'),
    path('ajout_facture',views.ajout_facture,name='ajout-facture'),
]