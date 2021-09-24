from datetime import date
ano = int(input("Insira o ano do seu nascimento: "))
idade = date.today().year - ano
print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, date.today().year))
if idade == 18:
    print("\033[31mHora de se alistar!!!\033[m")
elif idade < 18:
    saldo =  18 - idade
    print("\033[32mAinda vai se alistar. Faltam {} anos para o alistamento.\033[m".format(saldo))
    ano = date.today().year + saldo
    print("Seu alistamento sera em {}.".format(ano))
else:
    saldo = idade - 18
    print("\033[35mJá passou do tempo de alistamento.\nVocê deveria ter se alistado há {} anos.\033[m".format(saldo))
    ano = date.today().year - saldo
    print("Seu alistamento foi em {}.".format(ano))