n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n = (n1 + n2) / 2
print("A sua media foi: {:.1f}".format(n))
if n >= 6.0:
    print("Sua media foi boa! PARABÉNS!")
else:
    print("Sua media foi ruim! ESTUDE MAIS!")