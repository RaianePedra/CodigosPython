from datetime import date
maior = 0
menor = 0
atual = date.today().year
for a in range(1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu? ".format(a)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("No total {} são maiores de idade\nE {} ainda não atingiram a maior idade.".format(maior, menor))
