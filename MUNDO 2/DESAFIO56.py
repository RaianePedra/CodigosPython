totmulher = 0
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = " "
for p in range(1, 5):
    print("\033[36m----- {}ª PESSOA -----\033[m".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        nomevelho = nome
        maioridadehomem = idade
    if sexo in "Ff" and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print("A média da idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher))