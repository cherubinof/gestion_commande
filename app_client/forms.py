from django.forms import ModelForm
from.models import Client


class clientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'