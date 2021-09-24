'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
tot18 = totH = totM = 0
while True:
    idade = int(input("Qual a idade? "))
    sexo = str(input("Qual o sexo? [M/F]")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totH += 1
    if idade <= 20 and sexo == "F":
        totM += 1
    resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]

    if resp not in "S":
        break

print(f"\033[33m{tot18}\033[m Pessoas maiores de 18 anos.")
print(f"\033[34m{totH}\033[m Homens foram cadastrados.")
print(f"\033[35m{totM}\033[m Mulheres tem menos de 20 anos;")


