print("\033[32m {:-^30}\033[m".format("TABUADA"))
while True:
    num = int(input("Insira o valor desejado: "))
    print("-" * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} X {c} = {num * c}")
    print("-" * 30)
print("\033[32mFIM DO PROGRAMA. VOLTE SEMPRE\033[m")

















































































