#Print normal
"""
lanche = suco
print(lanche)
"""
#Tuplas sao imutaveis

#Como manipular as tuplas
"""
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[1:])
"""
#Ler quantos dados tem
"""
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")
print(len(lanche))
print("Comi pra caramba!!!")
"""

'''
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")
for comida in lanche:
    print(f"Eu vou vomer {comida}")
print("Comi pra caramba!!!")
'''
#Se precisar mostrar a posicao
'''
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata")
for cont in range(0, len(lanche)):
    #print(f"Eu vou comer {lanche[cont]} na posicao {cont}")
    #print(lanche[cont])
print("Comi pra caramba!!!")
'''
#Outro jeito de mostrar a posicao.
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicao {pos}")
    #print(lanche[cont])

print("Comi pra caramba!!!")
