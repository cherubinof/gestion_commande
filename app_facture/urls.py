from django.urls import path
from app_facture import views


urlpatterns = [
    path('facture',views.facture,name='facture'),
    path('error404',views.error404,name='404'),
    path('ajout_facture',views.ajout_facture,name='ajout-facture'),
    path('modifier_facture/<int:pk>',views.modifire_facture,name='modifier-facture'),
    path('supprimer_facture/<int:pk>',views.supprimer_facture,name='supprimer-facture'),
    path('detail_fact/<int:pk>',views.detail_fact,name='detail-fact'),
]