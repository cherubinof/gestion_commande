from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request,'app_produit/accueil.html')
