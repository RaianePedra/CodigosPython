'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
total = quant = menor = cont = 0
nomeprod = " "
while True:
    nomeprod = str(input("Insira o nome do produto: "))
    preco = float(input("Preço do produto: R$"))
    total += preco
    cont += 1
    if preco >= 1000:
        quant += 1
    if cont == 1 or preco < menor: #se o primeiro produto for o menor, menor recebe o preço, ou se o proximo preco for menor q o primeiro, menor recebe o preço e o nome do produto mais barato.
        menor = preco
        barato = nomeprod
    resp = " " #
    while resp not in "SN":#so vai passar se colocar sim ou nao, se nao vai ficar pedindo a resposta.
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print(f"{total:.2f}R$ Foi o total gasto na compra.")
print(f"A quantidade de produtos maiores que R$1000 foi: {quant}.")
print(f"E o produto mais barato foi o/a {barato}.")
print("{:-^40}".format(" FIM DA COMPRA "))
