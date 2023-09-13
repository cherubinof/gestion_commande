from django.contrib import admin
from.models import Commande

# Register your models here.


class CommandeAdmin(admin.ModelAdmin):
    list_display = ['client','produit','quantite','paye','date_cmde','status']
    list_filter = ['status']
admin.site.register(Commande, CommandeAdmin)