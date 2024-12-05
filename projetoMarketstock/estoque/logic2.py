class Produto:
    def __init__(self, nome, qttdEstoque, validade, marca, idFornecedor):
        self.__nome = nome
        self.__qttdEstoque = qttdEstoque
        self.__validade = validade
        self.__marca = marca
        self.__idFornecedor = idFornecedor

        def criarProduto(self):
            pass

        def buscarProduto(self):
            pass

        def alternarProduto(self):
            pass


class Movimentacoes:
    def __init__(self, idProduto, idUsuario, quantidade, dataHora):
        self.__idProduto = idProduto
        self.__idUsuario = idUsuario
        self.__quantidade = quantidade
        self.__dataHora = dataHora

    def movimentarProduto(self):
        pass

    def obterRelatorio(self):
        pass


class Usuario:
    def __init__(self, idUsuario, nome, cargo):
        self.__idUsuario = idUsuario
        self.__nome = nome
        self.__cargo = cargo

    def criarUsuario(self):
        pass

    def excluirUsuario(self):
        pass


class Aviso:
    def __init__(self, idProduto, idPrevisaoEscassez, tipo, texto, dataAviso):
        self.__idProduto = idProduto
        self.__idPrevisaoEscassez = idPrevisaoEscassez
        self.__tipo = tipo
        self.__texto = texto
        self.__dataAviso = dataAviso

    def enviarAviso(self):
        pass


class Fornecedor:
    def __init__(self, idFornecedor, nome, contato):
        self.__idFornecedor = idFornecedor
        self.__nome = nome
        self.__contato = contato

    def criarFornecedor(self):
        pass

    def alterarFornecedor(self):
        pass

    def excluirFornecedor(self):
        pass


class PrevisaoEscassez:
    def __init__(self, idPrevisaoEscassez, dataEscassez, idProduto):
        self.__idPrevisaoEscassez = idPrevisaoEscassez
        self.__dataEscassez = dataEscassez
        self.__idProduto = idProduto

    def obterPrevisao(self):
        pass
