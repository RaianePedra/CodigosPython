preço = float(input("\nSalario do funcionario: R$"))

aumento = preço + (preço * 15 / 100)

print("O seu novo salario será de R${:.2f}".format(aumento))