import random
al1 = str(input("Aluno 1: "))
al2 = str(input("Aluno 2: "))
al3 = str(input("Aluno 3: "))
al4 = str(input("Aluno 4: "))

lista = [al1, al2, al3, al4]
random.shuffle(lista)
print("A ordem sorteada para a apresentação será:")
print(lista)