cont = soma = 0
print("\033[31mINSIRA 999 SE DESEJA PARAR0\033[m")
while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    cont += 1
    soma += num

print(f"FIM!!! Você digitou {cont} vezes e a soma foi {soma}")