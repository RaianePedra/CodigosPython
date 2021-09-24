import random
al1 = str(input("Nome do aluno 1: "))
al2 = str(input("Nome do aluno 2: "))
al3 = str(input("Nome do aluno 3: "))
al4 = str(input("Nome do aluno 4: "))

print("-"*12)
print("1-{}\n2-{}\n3-{}\n4-{}".format(al1, al2, al3, al4))
print("-"*12)
print("O aluno sorteado foi: {}".format(random.choice([al1, al2, al3, al4])))


'''OUTRO JEITO
import random
al1 = str(input("\nNome do aluno 1: "))
al2 = str(input("Nome do aluno 2: "))
al3 = str(input("Nome do aluno 3: "))
al4 = str(input("Nome do aluno 4: "))

lista = [al1, al2, al3, al4]

print("\n1-{}\n2-{}\n3-{}\n4-{}".format(al1, al2, al3, al4))

escolhido = random.choice(lista)
print("\nO aluno sorteado foi: {}".format(escolhido))

'''