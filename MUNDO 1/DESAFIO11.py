larg = float(input("Largura da parede: "))
alt =  float(input("Altura da parede: "))

área = larg * alt

print("Você tem uma parede {} x {} e sua area é de {}m²".format(larg, alt, área))

tinta = área / 2

print("Quantidade de tinta necessaria: {}l".format(tinta))
