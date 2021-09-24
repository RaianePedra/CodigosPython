print("\033[36m{:=^40}\033[m".format(" DETECTOR DE PALINDROMO "))
frase = str(input("Digite a frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1] #no lugar do for
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("É palindromo")
else:
    print("Não é palindromo.")


'''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("É palindromo")
else:
    print("Não é palindromo.")
'''