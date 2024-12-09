from django.db import models
from django.utils import timezone


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def criar_fornecedor(self):
        """
        Cria um novo fornecedor no sistema.
        """
        self.save()

    def alterar_fornecedor(self, novo_nome, novo_contato):
        """
        Altera os dados do fornecedor.

        novo_nome: Novo nome do fornecedor.
        novo_contato: Novo contato do fornecedor.
        """
        self.nome = novo_nome
        self.contato = novo_contato
        self.save()

    def excluir_fornecedor(self):
        """
        Exclui o fornecedor do sistema.
        """
        self.delete()


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    qttd_estoque = models.IntegerField()
    validade = models.DateField()
    marca = models.CharField(max_length=100)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def criar_produto(self):
        """
        Cria um novo produto no sistema.
        """
        self.save()

    def buscar_produto(self, nome):
        """
        Busca um produto pelo nome.

        nome: Nome do produto.
            - Instância do produto se encontrado, caso contrário None.
        """
        try:
            return Produto.objects.get(nome=nome)
        except Produto.DoesNotExist:
            return None

    def alterar_produto(self, novo_nome=None, nova_qttd_estoque=None, nova_validade=None, nova_marca=None,
                        novo_fornecedor=None):
        """
        Altera os dados do produto.

        novo_nome: Novo nome do produto (opcional).
        nova_qttd_estoque: Nova quantidade em estoque (opcional).
        nova_validade: Nova data de validade (opcional).
        nova_marca: Nova marca do produto (opcional).
        novo_fornecedor: Novo fornecedor do produto (opcional).
        """
        if novo_nome:
            self.nome = novo_nome
        if nova_qttd_estoque is not None:
            self.qttd_estoque = nova_qttd_estoque
        if nova_validade:
            self.validade = nova_validade
        if nova_marca:
            self.marca = nova_marca
        if novo_fornecedor:
            self.fornecedor = novo_fornecedor
        self.save()


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def criar_usuario(self):
        """
        Cria um novo usuário no sistema.
        """
        self.save()

    def excluir_usuario(self):
        """
        Exclui o usuário do sistema.
        """
        self.delete()


class Movimentacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_hora = models.DateTimeField(default=timezone.now)

    def movimentar_produto(self):
        """
        Registra uma movimentação de produto no sistema.
        """
        # Atualiza a quantidade de produto no estoque
        self.produto.qttd_estoque += self.quantidade
        self.produto.save()
        # Salva a movimentação
        self.save()

    def obter_relatorio(self):
        """
        Gera um relatório das movimentações de produtos.
        QuerySet contendo todas as movimentações.
        """
        return Movimentacao.objects.all()


class PrevisaoEscassez(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_escassez = models.DateField()

    def obter_previsao(self):
        """
        Obtém a previsão de escassez do produto.
        Data prevista para a escassez do produto.
        """
        # Essa variável vai receber a média de vendas de um determinado produto por dia.
        taxa_consumo_diario = 80  # Exemplo: 80 unidade por dia
        dias_restantes = self.produto.qttd_estoque / taxa_consumo_diario
        self.data_escassez = timezone.now().date() + timezone.timedelta(days=dias_restantes)
        self.save()
        return self.data_escassez


class Aviso(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    previsao_escassez = models.ForeignKey(PrevisaoEscassez, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    texto = models.TextField()
    data_aviso = models.DateField(default=timezone.now)

    def enviar_aviso(self):
        """
        Envia um aviso sobre a previsão de escassez do produto.
        """
        # Lógica de envio de aviso (por exemplo, enviar um e-mail ou notificação)
        print(f"Aviso: {self.tipo} - {self.texto}")
