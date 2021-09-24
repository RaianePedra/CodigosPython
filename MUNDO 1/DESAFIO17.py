import math
co = float(input("Valor do cateto oposto: "))
ca = float(input("Valor do cateto adjacente: "))

print("O valor da hipotenusa sera: {:.2f}".format(math.hypot(co, ca)))
