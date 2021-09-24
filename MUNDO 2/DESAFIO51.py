cont = 0
print("=" * 40)
print("\033[36mOS 10 PRIMEIROS TERMOS DA PA\033[m")
print("=" * 40)
ptermo = int(input("Insira o primeiro termo: "))
razao = int(input("Razão: "))

dez = ptermo + (10 - 1) * razao

for c in range(ptermo, dez + razao, razao):
    cont = cont + 1
    print("{} - {}".format(cont, c))
print("\033[36mACABOU\033[m")