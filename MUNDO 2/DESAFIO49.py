num = int(input("Insira o numero que deseja saber a tabuada: "))
for c in range(0, 11):
    print("{} x {} = {}".format(num, c, num * c))