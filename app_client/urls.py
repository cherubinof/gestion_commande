from django.urls import path
from app_client import views

urlpatterns = [
    path('list_client',views.list_client,name='list-client'),
    path('detail_client/<int:pk>',views.detail_client,name='detail-client'),
]