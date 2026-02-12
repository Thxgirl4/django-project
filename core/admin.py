from django.contrib import admin

from .models import Product, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    search_fields = ('nome',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    search_fields = ('nome', 'sobrenome', 'email')

admin.site.register(Product, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
