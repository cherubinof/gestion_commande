from django.urls import path
from app_cmde import views


urlpatterns = [
    path('list_cmde',views.list_cmde,name='list-cmde'),
]