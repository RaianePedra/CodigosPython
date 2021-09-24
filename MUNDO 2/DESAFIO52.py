mult = 0
print("\033[36m{:=^60}\033[m".format(" DESCOBRINDO OS PRIMOS "))
num = int(input("Digite o numero: "))

for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end=" ")
        mult += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[mO número {} foi dividido {} vezes.".format(num, mult))

if (mult == 2):
    print("Por isso é primo!!!")
else:
    print("Por isso NÃO é primo!!!")