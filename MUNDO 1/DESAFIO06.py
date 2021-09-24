''' CORRETO '''
num = int(input("Insira o numero: "))
dob = num*2
tri = num*3
raiz = num ** (1/2)

print("O dobro desse numero sera: {}\nO triplo: {}\nE sua raiz quadradada: {:.2f}".format(dob, tri, raiz))

'''
===== OUTRO JEITO ======

num = int(input("Insira o numero: "))
print("O dobro desse numero sera: {}\nO triplo: {}\nE sua raiz quadradada: {:.2f}".format((num*2), (num*3), (num**(1/2))))

>>>

===== JEITO 2 ======

num = int(input("Insira o numero: "))
print("O dobro desse numero sera: {}\nO triplo: {}\nE sua raiz quadradada: {:.2f}".format((num*2), (num*3), pow(num, (1/2))))

'''