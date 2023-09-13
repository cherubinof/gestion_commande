from django.shortcuts import render,redirect
from .models import Produit
from app_cmde.models import Commande
from app_client.models import Client
from.forms import ProduitForm

# Create your views here.

def accueil(request):
    client = Client.objects.all()
    commande = Commande.objects.all()
    context = {
        'client':client,
        'commande':commande
    }
    return render(request,'app_produit/accueil.html',context)


def list_produit(request):
    produit = Produit.objects.all()
    produit_total = produit.count()
    context = {
        'produit':produit,
        'produit_total':produit_total
    }
    return render(request,'app_produit/list_produit.html',context)

def ajout_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-produit')
    else:
        form = ProduitForm()
    context = {
        'form':form
    }
    return render(request,'app_produit/ajout_produit.html',context)


def modifier_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('list-produit')
    else:
        form = ProduitForm(instance=produit)
    context = {
        'form':form
    }
    return render(request,'app_produit/modifier_produit.html',context)

def supprimer_produit(request,pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('list-produit')
    context = {
        'items':produit
    }
    return render(request,'app_produit/supprimer_produit.html',context)
