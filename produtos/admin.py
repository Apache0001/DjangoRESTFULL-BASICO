from django.contrib import admin

from .models import Produto, Avaliacao
# Register your models here.


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo','categoria', 'especificacoes', 'preco', 'desconto', 'url')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'nome','email', 'comentario', 'avaliacao')
