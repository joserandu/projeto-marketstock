from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def criar_fornecedor(self):
        pass

    def alterar_fornecedor(self):
        pass

    def excluir_fornecedor(self):
        pass


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    qttd_estoque = models.IntegerField()
    validade = models.DateField()
    marca = models.CharField(max_length=100)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def criar_produto(self):
        pass

    def buscar_produto(self):
        pass

    def alternar_produto(self):
        pass


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def criar_usuario(self):
        pass

    def excluir_usuario(self):
        pass


class Movimentacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_hora = models.DateTimeField()

    def movimentar_produto(self):
        pass

    def obter_relatorio(self):
        pass


class PrevisaoEscassez(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_escassez = models.DateField()

    def obter_previsao(self):
        pass


class Aviso(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    previsao_escassez = models.ForeignKey(PrevisaoEscassez, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    texto = models.TextField()
    data_aviso = models.DateField()

    def enviar_aviso(self):
        pass
