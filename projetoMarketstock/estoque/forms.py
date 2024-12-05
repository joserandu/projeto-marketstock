from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'qttd_estoque', 'validade', 'marca', 'fornecedor']
