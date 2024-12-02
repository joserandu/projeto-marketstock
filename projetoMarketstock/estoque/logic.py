from random import randint
import time

Class Produto:
  def __init__(nome, qtd, validade):
    self.__nome = nome
    self.__qtd = qtd
    self.__validade = validade
    # self.__media_vendas = media_vendas
    # self.__alerta_escasses = alerta_escasses
    # self.__tempo_restante = tempo_restante

  # Getters e Setters
  def getQtd():
    return qtd

  def setQtd(newQtd):
    self.__qtd = newQtd

  def getValidade():
    return validade

  def setValidade(newValidade):
    self.__validade = newValidade
"""
  def getMedia_vendas():
    return media_vendas

  def setMedia_vendas():
    self.__media_vendas = media_vendas

  def getAlerta_escasses():
    return alerta_escasses

  def setAlerta_escasses(newAlerta_escasses):
    self.__alerta_escasses = newAlerta_escasses

  def getTempo_restante():
    return tempo_restante

  def setTempo_restante(newTempo_restante):
    self.__tempo_restante = newTempo_restante
"""
  # Métodos

  @staticmethod
  def qtd_vendas():
    qtd = randint(0, 10)
    return qtd

  @staticmethod
  def calcular_media_vendas(): 
    media = randint(0, 10) / 1  # é nesse 10 que a gente controla quanto é vendido por hora

  def calcular_tempo_restante(self, media_vendas):
    pass

  def alertar_escasses(self, produto, tempo_restante):  // Já instanciado
    if (tempo_restante < 5):
      print(f"O produto: {produto} acabará em {tempo_restante}")

produto = Produto("Paçoca", 20, "20/12/2024")

def main(produto):
 
  lista_vendas = []

  while(produto.qtd >= 0):

    i = 1
    qtd = produto.qtd_vendas()
    vendas_hora = {"hora: ": i, "Quantidade de vendas: " = qtd}
    lista_vendas.append(vendas_hora)
    
    print(f"Quantidade de vendas na última  {i}: {qtd}")

    i += 1
    time.sleep(2)
    # media = produto.calcular_media_vendas()
    # printf(f"Media de vendas: ")

main(produto)
