from django.db import models
import uuid

# Create your models here.

class Produit(models.Model):
    code = models.CharField(max_length=100, blank=True)
    nom = models.CharField(max_length=100)
    prix = models.FloatField()
    
    
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if self.code == '':
            self.code = str(uuid.uuid4()).replace('','-').upper()[0:5]
            return super().save(*args, **kwargs)
    
    
 
