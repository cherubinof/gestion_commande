from django.shortcuts import render
from .models import Commande

# Create your views here.

def list_cmde(request):
    commande = Commande.objects.all()
    total_commande = commande.count()
    context = {
        'commande':commande,
        'total_commande':total_commande
    }
    return render(request,'app_cmde/list_cmde.html',context)
