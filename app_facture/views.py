from django.shortcuts import render

# Create your views here.


def facture(request):
    return render(request,'app_facture/facture.html')
