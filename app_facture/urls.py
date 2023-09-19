from django.urls import path
from app_facture import views


urlpatterns = [
    path('facture',views.facture,name='facture'),
    path('detail_fact',views.detail_fact,name='detail-fact'),
    path('ajout_facture',views.ajout_facture,name='ajout-facture'),
    path('modifier_facture/<int:pk>',views.modifire_facture,name='modifier-facture'),
    path('supprimer_facture/<int:pk>',views.supprimer_facture,name='supprimer-facture'),
]