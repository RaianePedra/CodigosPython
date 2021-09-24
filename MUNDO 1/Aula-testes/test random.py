'''import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
print('Sorteio: {}'. format(random.choice([a1, a2, a3, a4])))'''

'''escolhe um numero aleatorio entre 0 e 5
import random
print(random.randint(0, 5))'''

'''from random import sample
nome = input('Digite algo: ')
a = sample(nome,len(nome))
print(a)

====== SEGUNDO JEITO

from random import sample
def embaralha(nome):
    a = sample(nome,len(nome))
    d = ''.join(a)
    print(a)
    print(d.lower())
'''

nome = input('Digite algo: ')
embaralha(nome)
'''import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('Ordem de apresentação:')
print(lista)'''