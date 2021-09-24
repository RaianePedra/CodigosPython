''' COMUM, DEFINIDO
cont = 1
while cont <= 10:
    print(cont, "->", end=" ")
    cont += 1
print("ACABOU")
'''

''' VAI CONTAR INFINITAMENTE
cont = 1
while True:
    print(cont, "->", end=" ")
    cont += 1
print("ACABOU")
'''
n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n
print("A soma vale {}".format(s))