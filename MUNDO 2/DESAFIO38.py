print("\033[31mObs: Os números inseridos devem ser inteiros.\033[m")
num = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num > num2:
    print("O primeiro valor é o maior.")
elif num2 > num:
    print("O segundo valor é o maior.")
else:
    print("Não existe valor maior, os dois são iguais.")