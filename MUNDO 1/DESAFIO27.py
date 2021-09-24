"""LER O NOME COMPLETO DA PESSOA E MOSTRAR SEPARADAMENTE O PRIMEIRO E ULTIMO NOME SEPARADOS
EX: ANA MARIA DE SOUZA
    PRIMEIRO: ANA
    ULTIMO: SOUZA
"""
n = str(input("Insira seu nome completo: ")).strip()
nome = n.split()
print("Primeiro nome: {}".format(nome[0]))
print("Ultimo nome: {}".format(nome[-1]))

'''
>>> Outro jeito
print("Ultimo nome: {}".format(nome[len(nome)-1]))

len de nome vai saber quantas posicoes tem,
 mostrar o nome na posicao de len de nome, -1 '''
