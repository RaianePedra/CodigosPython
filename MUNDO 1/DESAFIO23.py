''' LEIA UM NUMERO DE 0-999 E MOSTRAR O NUMERO SEPARADO
EX: numero digitado 1834
    unidade 4
    dezena 3
    centena 8
    milhar 1
'''
num = int(input("Insira um numero de 0 a 999: "))
u = num//1 % 10
d = num//10 % 10
c = num //100 % 10
m = num//1000 % 10
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

''' OBSERVACAO'''