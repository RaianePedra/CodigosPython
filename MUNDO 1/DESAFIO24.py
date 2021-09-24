''' lER O NOME DA CIDADE E DIZER SE COMECOU OU NAO COM "SANTO"'''
cidade = str(input("Insira o nome da cidade: ")).strip()
print(cidade[:5].upper() == "SANTO")
