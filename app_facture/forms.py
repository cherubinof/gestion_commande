from django.forms import ModelForm
from django import forms
from.models import Facture



class FactureForm(ModelForm):
    class Meta:
        model = Facture
        fields = '__all__'