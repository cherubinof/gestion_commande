from django.shortcuts import render,redirect
from .models import Commande
from.forms import CommadeForm

# Create your views here.

def list_cmde(request):
    commande = Commande.objects.all().order_by('-id')
    total_commande = commande.count()
    context = {
        'commande':commande,
        'total_commande':total_commande
    }
    return render(request,'app_cmde/list_cmde.html',context)

def ajout_cmde(request):
    if request.method == 'POST':
        form = CommadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-cmde')
    else:
        form = CommadeForm()
    context = {
        'form':form
    }
    return render(request,'app_cmde/ajout_cmde.html',context)

def modifier_cmde(request,pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        form = CommadeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('list-cmde')
    else:
        form = CommadeForm(instance=commande)
    context = {
        'form':form
    }
    return render(request,'app_cmde/modifier_cmde.html',context)

def supprimer_cmde(request,pk):
    commande = Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('list-cmde')
    context = {
        'items':commande
    }
    return render(request,'app_cmde/supprimer_cmde.html',context)


def stat(request):
    return render(request,'app_cmde/stat.html')
