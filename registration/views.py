from django.shortcuts import render
from.forms import InscriptionForm

# Create your views here.

def Inscription(request):
    return render(request,'registration/register.html')
