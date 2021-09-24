'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5 e R$1.'''
print("=" * 45)
print("{:^50}".format("\033[34mBEM-VINDO AO BANCO PEDRA'S\033[m"))
print("=" * 45)
valor = int(input("Insira o valor que deseja sacar: R$"))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de \033[33m{totced}\033[m cedulas de \033[32m{ced}R$\033[m")
        if ced == 100:
             ced = 50
        elif ced == 50:
             ced = 20
        elif ced == 20:
             ced = 10
        elif ced == 10:
             ced = 5
        elif ced == 5:
             ced = 1
        totced = 0
        if total == 0:
            break
print("=" * 45)
print("{:^55}".format("\033[34mVOLTE SEMPRE AO BANCO PEDRA'S!!!\033[m"))
print("=" * 45)0