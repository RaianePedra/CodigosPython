from random import randint
from time import sleep
itens = ["Pedra", "Papel", "Tesoura"]
computador = randint(0, 2)
print("\033[36m{:=^60}\033[m".format(" JOKENPÔ "))
print("Suas opções são:\n[ 0 ]Pedra\n[ 1 ]Papel\n[ 2 ]Tesoura")
jog = int(input("Qual deseja escolher, jogador? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print("-=" * 50)
print("O computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jog]))
print("-=" * 50)

if computador == 0: #PEDRA
    if jog == 0: #PEDRA
        print("EMPATE")
    elif jog ==1: #PAPEL
        print("JOGADOR VENCE")
    elif jog == 2: #TESOURA
        print("COMPUTADOR VENCE")
elif computador ==1: #PAPEL
    if jog == 0: #PEDRA
        print("COMPUTADOR VENCE")
    elif jog == 1: #PAPEL
        print("EMPATE")
    elif jog == 2: #TESOURA
        print("JOGADOR VENCE")
elif computador == 2: #TESOURA
    if jog == 0: #PEDRA
        print("JOGADOR VENCE")
    elif jog == 1: #PAPEL
        print("COMPUTADOR VENCE")
    elif jog == 2: #TESOURA
        print("EMPATE")
