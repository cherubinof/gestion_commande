from django.shortcuts import render,redirect
from .models import Client
from app_cmde.models import Commande
from.forms import clientForm

# Create your views here.


def list_client(request):
    client = Client.objects.all().order_by('-id')
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


def ajout_client(request):
    if request.method == 'POST':
        form = clientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-client')
    else:
        form = clientForm()
    context = {
        'form':form
    }
    return render(request,'app_client/ajout_client.html',context)

def modifier_client(request,pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        form = clientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('list-client')
    else:
        form = clientForm(instance=client)
    context = {
        'form':form
    }
    return render(request,'app_client/modifier_client.html',context)

def supprimer_client(request,pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('list-client')
    context = {
        'items':client
    }
    return render(request,'app_client/supprimer_client.html',context)


def suprimmer_all(request,pk):
    if request.method =='POST':
        client_id = request.POST.getlist('id[]')
        for id in client_id:
            client = Client.objects.get(id=pk)
            client.delete()
            return redirect('list-client')
    return render(request,'app_client/suo_all.html')

