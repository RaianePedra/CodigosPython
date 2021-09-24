'''
nome = input("Qual o seu nome?")
print("Prazer em te conhecer {:>20}!". format(nome))
{:=^20} ==========nome==========
{:^20} centraliza
{:>20} direita
{:<^20} esquerda
'''

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

'''end="" pra dar continuidade'''

print("A soma vale: {}\nO produto: {}\nA divisao: {:.3}".format(s, m, d), end=' ')
print("Divisao inteira:{}\nE potencia:{}". format(di, e))