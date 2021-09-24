from random import randint
from time import sleep
num = randint(0,5)
print("-=-" * 20)
print("Vou pensar em um numero de 0 a 5 tente adivinhar...")
print("-=-" * 20)
resp = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if resp == num:
    print("VOCÊ ACERTOU, PARABENS!!!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}!".format(num, resp))

