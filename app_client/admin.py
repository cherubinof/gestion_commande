from django.contrib import admin
from.models import Client

# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ['noms','telephone','ville']
    list_filter = ['noms']
admin.site.register(Client, ClientAdmin)
