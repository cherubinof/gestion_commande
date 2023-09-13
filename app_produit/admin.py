from django.contrib import admin
from.models import Produit,Tag

# Register your models here.


class ProduitAdmin(admin.ModelAdmin):
    list_display = ['code','nom','stock','prix',]
    list_filter = ['nom']
admin.site.register(Produit,ProduitAdmin)

admin.site.register(Tag)
