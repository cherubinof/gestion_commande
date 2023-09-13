from django.shortcuts import render
from .models import Client
from app_cmde.models import Commande

# Create your views here.


def list_client(request):
    client = Client.objects.all()
    total_client = client.count()
    context = {
        'client':client,
        'total_client':total_client
    }
    return render(request,'app_client/list_client.html',context)



def detail_client(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    context = {
        'client':client,
        'commande':commande,
        'commande_total':commande_total
    }
    return render(request,'app_client/detail_client.html',context)
