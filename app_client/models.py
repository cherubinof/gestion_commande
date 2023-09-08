from django.db import models

# Create your models here.


class Client(models.Model):
    noms = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    ville = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.noms
