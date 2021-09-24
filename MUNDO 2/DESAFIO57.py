sexo = str(input("Informe seu sexo: [F/M]")).upper()
while sexo not in "MmFf": #nao esta em Mm ou Ff
    print("\033[31mDados inválidos. Tente novamente!\033[m")
    sexo = str(input("Informe o sexo : [F/M]")).upper()
print("Sexo {} registrado com sucesso.".format(sexo))
