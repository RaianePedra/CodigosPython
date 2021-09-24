import math
ang = float(input("Insira o valor do ângulo: "))

print("O valor do seno é:{:.2f}\nDo cosseno: {:.2f}\nDa tangente:{:.2f}".format(math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))