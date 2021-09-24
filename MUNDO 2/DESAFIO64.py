num = cont = soma = 0
print("\033[31mDigite 999 se deseja parar\033[m")
num = int(input("Digite um numero: ")) #ler o flag do lado de fora

while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um numero: ")) # e ler o flag do lado de dentro
print("Você digitou {} números".format(cont))
print("A soma dos numeros digitados foi {}".format(soma))
print("ACABOU")