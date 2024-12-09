from django.contrib import admin
from .models import Fornecedor, Produto, Usuario, Movimentacao, PrevisaoEscassez, Aviso


class FornecedorAdmin(admin.ModelAdmin):
    """
    Essas funções dessa classe não serão utilizadas nesse momento pois elas são facilmente controladas na área
    administrativa do django, que é nosso foco antes de inserí-las no dashboard HTML.
    """
    list_display = ('nome', 'contato')


class ProdutoAdmin(admin.ModelAdmin):
    """
    As funções dessa classe também não serão descritas aqui pois elas são facilmente manipuladas na área
    administrativa do django.
        - Obs: Para pesquisar um produto, tecle Ctrl + F
    """
    list_display = ('nome', 'qttd_estoque', 'validade', 'marca', 'fornecedor')


class UsuarioAdmin(admin.ModelAdmin):
    """
    As funções estão no admin do django.
    """
    list_display = ('nome', 'cargo')


class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'usuario', 'quantidade', 'data_hora')


class PrevisaoEscassezAdmin(admin.ModelAdmin):
    list_display = ('produto', 'data_escassez')
    actions = ['calcular_previsao_escassez']

    def calcular_previsao_escassez(self, request, queryset):
        for previsao in queryset:
            data_escassez = previsao.obter_previsao()
            self.message_user(request, f'Previsão de escassez para {previsao.produto.nome}: {data_escassez}')

    calcular_previsao_escassez.short_description = 'Calcular Previsão de Escassez'


class AvisoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'previsao_escassez', 'tipo', 'texto', 'data_aviso')


admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Movimentacao, MovimentacaoAdmin)
admin.site.register(PrevisaoEscassez, PrevisaoEscassezAdmin)
admin.site.register(Aviso, AvisoAdmin)
