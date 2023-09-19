from django.shortcuts import render,redirect
from .models import Facture
from.forms import FactureForm

# Create your views here.


def facture(request):
    facture = Facture.objects.all().order_by('-id')
    facture_count = facture.count()
    context = {
        'facture':facture,
        'facture_count':facture_count
    }
    return render(request,'app_facture/facture.html',context)


def ajout_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facture')
    else:
        form = FactureForm()
    context = {
        'form':form
    }
    return render(request,'app_facture/ajout_facture.html',context)


def modifire_facture(request,pk):
    facture = Facture.objects.get(id=pk)
    if request.method == 'POST':
        form = FactureForm(request.POST,instance=facture)
        if form.is_valid():
            form.save()
            return redirect('facture')
    else:
        form = FactureForm(instance=facture)
    context = {
        'form':form
    }
    return render(request,'app_facture/modifier_facture.html',context)


def supprimer_facture(request,pk):
    facture = Facture.objects.get(id=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('facture')
    context = {
        'tems':facture
    }
    return render(request,'app_facture/supprimer_facture.html',context)


def detail_fact(request):
    return render(request,'app_facture/detail_fact.html')
