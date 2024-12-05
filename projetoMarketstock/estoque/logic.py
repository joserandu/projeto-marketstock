from random import randint
import time

class Produto:
    def __init__(self, nome, qtd, validade):
        self.__nome = nome
        self.__qtd = qtd
        self.__validade = validade

    # Getters e Setters
    def getQtd(self):
        return self.__qtd

    def setQtd(self, newQtd):
        self.__qtd = newQtd

    def getValidade(self):
        return self.__validade

    def setValidade(self, newValidade):
        self.__validade = newValidade

    # Métodos
    def qtd_vendas(self):
        qtd = randint(0, 10)
        return qtd

    def calcular_media_vendas(self):
        media = randint(0, 10) / 1  # Retorna a média de vendas
        return media

    def calcular_tempo_restante(self, media_vendas):
        pass

    def alertar_escasses(self, tempo_restante):
        if tempo_restante < 5:
            print(f"O produto: {self.__nome} acabará em {tempo_restante} unidades")

def main(produto):
    lista_vendas = []
    i = 1  # Inicializa o contador da hora
    while produto.getQtd() > 0:  # Enquanto o estoque for maior que 0
        qtd = produto.qtd_vendas()  # Obtém a quantidade vendida
        produto.setQtd(produto.getQtd() - qtd)  # Atualiza a quantidade em estoque
        vendas_hora = {"hora": i, "qtd": qtd}
        lista_vendas.append(vendas_hora)
        
        
        print(f"Quantidade de vendas na hora {i}: {qtd}")

        i += 1
        time.sleep(1)
    
    print("Vendas realizadas:", lista_vendas)

produto = Produto("Paçoca", 20, "20/12/2024")
main(produto)  # Agora a função main pode ser chamada para executar a simulação
