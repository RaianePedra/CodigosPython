''' CONDICOES SIMPLES E COMPOSTAS '''

tempo = int(input("Quantos anos tem seu carro? "))
''' Jeito normal
if tempo <= 3:
    print("Carro novo")
else:
    print("Carro velho") '''
'''Simplificado'''
print("Carro Novo" if tempo<3 else "Carro Velho")