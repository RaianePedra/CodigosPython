print("\033[36mVamos calcular o seu IMC e mostrar seu status.\033[m")
peso = float(input("Peso: {Kg}"))
alt = float(input("Altura: {m}"))

imc = peso / (alt ** 2)

print("IMC = {:.2f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está no peso ideal!!!")
elif imc >= 25 and imc <= 30:
    print("Você esta em sobrepeso.")
elif imc >= 30 and imc <= 40:
    print("Obesidade.")
else:
    print("\033[31mVocê está em obesidade mórbida, cuidado!!!\033[m")