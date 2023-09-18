from django.urls import path
from app_cmde import views


urlpatterns = [
    path('list_cmde',views.list_cmde,name='list-cmde'),
    path('ajout_cmde',views.ajout_cmde,name='ajout-cmde'),
    path('modifier_cmde/<int:pk>',views.modifier_cmde,name='modifier-cmde'),
    path('supprimer_cmde/<int:pk>',views.supprimer_cmde,name='supprimer-cmde'),
    path('stat',views.stat,name='stat'),
]