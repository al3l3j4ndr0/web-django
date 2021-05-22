from django.contrib import admin

from floresApp.models import cliente,producto

class userAdminFiltro(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono", "email")
    search_fields= ("nombre", "email")

class articulosAdminFiltro(admin.ModelAdmin):
    list_filter =("nombre",)

admin.site.register(cliente, userAdminFiltro)
admin.site.register(producto, articulosAdminFiltro)

# Register your models here.
