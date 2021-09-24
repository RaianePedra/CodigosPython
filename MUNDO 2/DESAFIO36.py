casa = float(input("Valor da casa: "))
sal = float(input("Seu salário: "))
anos = int(input("Em quantos anos pretende pagar?"))

minimo = sal * 30 / 100
print("A parcela não pode ser maior que {:.2f}".format(minimo))

mes = casa / (anos * 12)
print("O valor da parcela por mês sera de: R${:.2f}".format(mes))

if mes > minimo:
    print("\n\033[31mEmprestimo negado\033[m")
else:
    print("\n\033[33mParabéns! Emprestimo aceito\033[m")