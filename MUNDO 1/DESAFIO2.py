al = input("\nInsira algo: ")
print("\nO tipo primitivo do valor {}, sera:".format(al),type(al))
print(f"So tem espaco? {al.isspace()}")
print(f"Numero? {al.isnumeric()}")
print(f"Alfabetico? {al.isalpha()}")
print(f"Alfabetico e numero? {al.isalnum()}")
print(f"Maiuscula? {al.isupper()}")
print(f"Minuscula? {al.islower()}")
print(f"Capitalizada? {al.istitle()}")