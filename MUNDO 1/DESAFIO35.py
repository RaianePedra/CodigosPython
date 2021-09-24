print("-=-" * 20)
print("Analisando Triângulos")
print("-=-" * 20)

r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("\nPodem formar um triângulo!!!")
else:
    print("\nNão podem formar um triângulo!")
