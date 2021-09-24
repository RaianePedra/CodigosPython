vel = float(input("Qual a velocidade? "))
multa = (vel - 80) * 7

if vel >= 80:
    print("MULTADO! Você excedeu o limite permitido de 80km/h")
    print("O valor da multa será de: {:.2f}R$".format(multa))

print("Tenha um bom dia! Dirija com cuidado!")