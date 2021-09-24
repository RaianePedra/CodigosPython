from random import randint
from time import sleep
computador = randint(0, 10)
print("-=-" * 20)
print("\033[35mOlá, sou seu computador... \nAcabei de pensar em um numero de 0 a 10\ntente adivinhar qual foi...\033[m")
print("-=-" * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Em que número eu pensei? "))
    print("\033[33mPROCESSANDO...\033[m")
    sleep(2)
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
print("\n\033[36mBOA! Você acertou com o {}° palpite(s). Parabéns!!!\033[m".format(palpites))
