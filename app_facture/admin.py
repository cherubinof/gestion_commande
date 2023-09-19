from django.contrib import admin
from.models import Facture

# Register your models here.



class FactureAdmin(admin.ModelAdmin):
    list_display = ['client','commande','date_facture','type_facture']
    list_filter = ['client']
admin.site.register(Facture,FactureAdmin)
