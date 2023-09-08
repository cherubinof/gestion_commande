from django.db import models
from app_produit.models import Produit
from app_client.models import Client

# Create your models here.



class Commande(models.Model):
    STATUT_CHOICE = (
        ('Livrer', 'Livrer'),
        ('Nom_livrer', 'Nom_livrer'),
        ('En_attenta', 'En_attente')
    )
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=STATUT_CHOICE)
    date_cmde = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status
