from django.shortcuts import render,redirect
from.forms import InscriptionForm

# Create your views here.

def Inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = InscriptionForm()
    context = {
        'form':form
    }
    return render(request,'registration/register.html',context)

# def connextion(request):
#     return render(request,'registration/login.html')
