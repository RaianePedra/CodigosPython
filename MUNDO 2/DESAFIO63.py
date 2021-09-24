print("-=-" * 10)
print("SEQUÊNCIAA DE FIBONACCI")
print("-=-" * 10)
num = int(input("Insira até onde deseja saber a sequência: "))
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2), end="")
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(" -> {}".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print(" -> FIM", end="")


































