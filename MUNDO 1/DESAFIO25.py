"""LER O NOME DE UMA PESSOA E DIZER SE TEM "SILVA" NO  NOME"""
nome = str(input("Insira o nome: ")).strip()
print("Tem Silva? {}".format("silva" in nome.lower()))
