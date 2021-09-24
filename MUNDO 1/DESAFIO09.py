'''Correto, porem muito prolongado
print("======== TABUADA =========")
tab = int(input("Entre com o numero que deseja saber: "))
n1 = tab * 1
n2 = tab * 2
n3 = tab * 3
n4 = tab * 4
n5 = tab * 5
n6 = tab * 6
n7 = tab * 7
n8 = tab * 8
n9 = tab * 9
n10 = tab * 10
print("{} x {} = {}".format(tab, 1, n1))
print("{} x {} = {}".format(tab, 2, n2))
print("{} x {} = {}".format(tab, 3, n3))
print("{} x {} = {}".format(tab, 4, n4))
print("{} x {} = {}".format(tab, 5, n5))
print("{} x {} = {}".format(tab, 6, n6))
print("{} x {} = {}".format(tab, 7, n7))
print("{} x {} = {}".format(tab, 8, n8))
print("{} x {} = {}".format(tab, 9, n9))
print("{} x {} = {}".format(tab, 10, n10))'''

''' NOVO JEITO - MAIS SUCINTO '''
print("======== TABUADA =========")
tab = int(input("Entre com o numero que deseja saber: "))
print("-" * 12)
print("{} x {} = {}".format(tab, 1, tab*1))
print("{} x {} = {}".format(tab, 2, tab*2))
print("{} x {} = {}".format(tab, 3, tab*3))
print("{} x {} = {}".format(tab, 4, tab*4))
print("{} x {} = {}".format(tab, 5, tab*5))
print("{} x {} = {}".format(tab, 6, tab*6))
print("{} x {} = {}".format(tab, 7, tab*7))
print("{} x {} = {}".format(tab, 8, tab*8))
print("{} x {} = {}".format(tab, 9, tab*9))
print("{} x {} = {}".format(tab, 10, tab*10))
print("-" * 12)