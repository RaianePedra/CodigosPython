'''ler o nome completo de uma pessoa
A - mostrar todas as letras maiusculas
B - mostrar todas as letras minusculas
C - Quantas letras ao todo sem considerar os espacos
D - Quantas letras tem o primeiro nome
'''

nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome: ")
print("Maiusculas: {}".format(nome.upper()))
print("Minusculas: {}".format(nome.lower()))

print("Quantidade de letras ao todo: {}".format(len(nome)-nome.count(" ")))
print("Primeiro nome tem: {}".format(nome.find(" ")))
separa = nome.split()
print("Primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))
