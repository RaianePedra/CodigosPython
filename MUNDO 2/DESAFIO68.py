'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.'''

from random import randint
soma = vitoria =0
while True:
    jog = int(input("Qual número deseja jogar? "))
    comp = randint(0, 10)
    soma = jog + comp

    resp = " " #
    while resp not in "PI": #
        resp = str(input("PAR OU IMPAR? [P/I] ")).strip().upper()[0]#

    print(f"Jogador jogou {jog} e o computador {comp}. A soma dos números jogados foi {soma}", end=" ")
    print("\033[31mDEU PAR\033[m" if soma % 2 == 0 else "\033[31mDEU IMPAR\033[m")

    if resp == "P":
        if soma % 2 == 0:
            print("\033[33mVocê Venceu. Parabéns!!!\033[m")
            vitoria += 1
        else:
            print("\033[31mVocê Perdeu. Que pena!\033[m")
            break
    elif resp == "I":
        if soma % 2 == 1:
            print("\033[33mVocê Venceu. Parabéns!!!\033[m")
            vitoria += 1
        else:
            print("\033[31mVocê Perdeu. Que pena!\033[m")
            break
    print("Vamos jogar novamente...")
print(f"\033[31mGAME OVER!!!\033[m Você venceu {vitoria} vezes.")