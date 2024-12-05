from django.urls import path
from .views import index, criar_produto

# As rotas da aplicação core ficarão aqui:
urlpatterns = [
    path('', index, name="index"),
    path('produto/criar/', criar_produto, name='criar_produto'),
]
