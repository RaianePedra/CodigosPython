sal = float(input("Qual o valor do seu salário: R$"))
if sal > 1250:
    novo = sal + (sal * 10 / 100)
else:
    novo = sal + (sal * 15 / 100)

print("O salário atual será de: {:.2f}R$".format(novo))
