from django.db import models
from app_produit.models import Produit
from app_client.models import Client

# Create your models here.



class Commande(models.Model):
    STATUT_CHOICE = (
        ('Livrer', 'Livrer'),
        ('Non_livrer', 'Non_livrer'),
        
    )
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)
    paye = models.BooleanField(default=False)
    status = models.CharField(max_length=100,choices=STATUT_CHOICE)
    date_cmde = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.status
