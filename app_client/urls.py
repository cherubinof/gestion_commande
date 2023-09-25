from django.urls import path
from app_client import views

urlpatterns = [
    path('list_client',views.list_client,name='list-client'),
    path('detail_client/<int:pk>',views.detail_client,name='detail-client'),
    path('ajout_client',views.ajout_client,name='ajout-client'),
    path('modifier_client/<int:pk>',views.modifier_client,name='modifier-client'),
    path('supprimer_client/<int:pk>',views.supprimer_client,name='supprimer-client'),
    path('delet_all',views.suprimmer_all,name='delete_all'),
]