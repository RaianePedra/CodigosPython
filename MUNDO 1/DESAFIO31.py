dist = float(input("Qual a distância da sua viagem em KM? "))
print("Você esta prestes a começar uma viagem de {}Km.".format(dist))

if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45

print("O preço da passagem será de: R${:.2f}".format(preço))