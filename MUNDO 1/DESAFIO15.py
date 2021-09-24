km = int(input("Quantos Km foram percorridos?"))
dias = float(input("Por quantos dias foi alugado?"))

valorkm = km * 0.15
valordias = dias * 60

print("\nPor dia ira pagar: R${}".format(valordias))
print("KM rodados no total: R${}".format(valorkm))
print("-"*28)
print("Ira pagar: R${:.2f}".format(valorkm+valordias))