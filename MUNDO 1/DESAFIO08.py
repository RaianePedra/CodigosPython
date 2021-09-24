''' Errado, pois a conta inserida era a atual e nao metros dividindo pelo numero'''
metros = float(input("Qual a distância em metros? "))
centi = metros * 100
mili = metros * 1000

print("{} metros em centimetros sera {:.0f}cm e em milimetros {:.0f}mm".format(metros, centi, mili))

''' ===== ATUALIZAÇÃO =====

- Fazer a operacao em km, hm, dm, cm, mm

'''
metros = float(input("Qual a distância em metros? "))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print("{} metros em:\nEm quilometros sera: {}km\nEm hectômetros: {}hm\nEm decâmetros: {}dam".format(metros, km, hm, dam))
print("Em decimetros: {}dm\nEm centimetros: {}cm\nEm milimetros: {}mm".format(dm, cm, mm))
