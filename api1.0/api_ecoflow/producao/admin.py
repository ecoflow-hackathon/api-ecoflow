from django.contrib import admin
from producao.models.produtor import Produtor
from producao.models.lote import Lote
from producao.models.informacao import InformacaoProducao

@admin.register(Produtor)
class ProdutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'criado_em')
    search_fields = ('identificador',)
    filter_horizontal = ('produtores',)

@admin.register(InformacaoProducao)
class InformacaoProducaoAdmin(admin.ModelAdmin):
    list_display = ('lote', 'produtor', 'descricao')
    search_fields = ('lote__identificador', 'produtor__nome')
