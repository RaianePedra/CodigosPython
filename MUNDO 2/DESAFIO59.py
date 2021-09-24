from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print("[1] Somar \n[2] Multiplicar \n[3] Maior\n[4] Novos números\n[5] Sair do programa")
    opcao = int(input(">>>>> Opção desejada: "))
    if opcao == 1:
        soma = n1 + n2
        print("=-=" * 15)
        print("A soma entre {} e {} é {}".format(n1, n2, soma))
    elif opcao == 2:
        prod = n1 * n2
        print("=-=" * 15)
        print("O produto entre {} e {} é {}".format(n1, n2, prod))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("=-=" * 15)
        print("Entre {} e {} o maior valor será {}".format(n1, n2, maior))
    elif opcao == 4:
        print("=-=" * 15)
        print("Informe os números novamente:")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Saindo...")
    else:
        print("\033[31mOpção inválida. Tente novamente.\033[m")
    sleep(2)

print("=-=" * 15)
print("\033[36mFim do programa. Volte sempre!!!\033[m")
print("=-=" * 15)
