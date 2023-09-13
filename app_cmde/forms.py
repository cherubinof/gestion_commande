from django.forms import ModelForm
from.models import Commande


class CommadeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'