from django.db import models
from app_client.models import Client
from app_cmde.models import Commande

# Create your models here.

class Facture(models.Model):
    TYPE_FACTURE = (
        ('R','Recu'),
        ('P','Performancefacture'),
        ('F','Facture')
    )
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande,on_delete=models.CASCADE)
    type_facture = models.CharField(max_length=1, choices=TYPE_FACTURE)
    total = models.DecimalField(max_digits=10000, decimal_places=2) 
    date_facture = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField()
