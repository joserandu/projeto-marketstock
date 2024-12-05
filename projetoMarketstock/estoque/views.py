from django.shortcuts import render, redirect
from .forms import ProdutoForm


def index(request):
    return render(request, 'index.html')


def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')  # Redirecione para a lista de produtos ou outra página apropriada
    else:
        form = ProdutoForm()

    return render(request, 'criar_produto.html', {'form': form})
