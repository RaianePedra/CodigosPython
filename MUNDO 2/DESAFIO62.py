print("=" * 40)
print("\033[36mDESCUBRA OS TERMOS DA PA\033[m")
print("=" * 40)
primeiro = int(input("Insira o primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos mais você quer?"))
print("\033[36mACABOU!!! No total foram {} termos.\033[m".format(total))