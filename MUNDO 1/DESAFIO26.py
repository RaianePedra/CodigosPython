'''
    LER UMA FRASE
    A-QUANTAS VEZES APARECE "A"
    B-POSICAO QUE ELA APARECE NA PRIMEIRA VEZ
    C-POSICAO QUE ELA APARECE NA ULTIMA VEZ
'''

frase = str(input("Digite a frase: ")).upper().strip()

print("Vezes que A aparece na frase: {}".format(frase.count("A")))
print("A primeira letra A apareceu na posicao: {}".format(frase.find("A")+1))
print("A ultima letra A apareceu na posicao: {}".format(frase.rfind("A")+1))



