from django.forms import ModelForm
from django import forms
from.models import Facture
from django.forms import fields, widgets
from django.utils.translation import gettext,gettext_lazy as _



class FactureForm(ModelForm):
   
    
    commentaire=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Facture
        fields = '__all__'
        
        
       
    