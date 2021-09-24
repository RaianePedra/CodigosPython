print("\033[34m-=-\033[m" * 20)
print("Analisando Triângulos")
print("\033[34m-=-\033[m" * 20)

r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("\033[30mPodem formar um triângulo!!!\033[m")
    print("\033[30mFormará o triângulo: \033[m")
    if r1 == r2 and r2 == r3:
        print("Equilátero! Possui todos os lados iguais.")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("Escaleno! Possui todos os lados diferentes.")
    else:
        print("Isoceles! Possui apenas dois lados iguais.")
else:
    print("\n\033[31mNão podem formar um triângulo!\033[m")