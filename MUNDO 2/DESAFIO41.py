from datetime import date
ano = int(input("Para saber a categoria é necessário\nque insira o seu ano de nascimento: "))
idade = date.today().year - ano
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("\n\033[33mClassificação: MIRIM")
elif idade <= 14:
    print("\n\033[33mClassificação: INFANTIL")
elif idade <= 19:
    print("\n\033[33mClassificação: JUNIOR")
elif idade <= 25:
    print("\n\033[33mClassificação: SÊNIOR")
else:
    print("\n\033[33mClassificação: MASTER")