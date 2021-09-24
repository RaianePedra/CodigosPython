i = 1
cont = 1
print("=" * 40)
print("\033[36mOS 10 PRIMEIROS TERMOS DA PA\033[m")
print("=" * 40)
ptermo = int(input("Insira o primeiro termo: "))
razao = int(input("Razão: "))
termo = ptermo

while cont <= 10:
    print("{}-> {} ".format(i, termo))
    termo += razao
    cont += 1
    i += 1
print("\033[36mACABOU\033[m")