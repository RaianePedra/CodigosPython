'''
nome = "Jose"
idade = 33
print(f"O {nome} tem {idade} anos.") #python 3.6...
print("O {} tem {} anos.".format(nome, idade)) #Python 3
print("O %s tem %d anos." %(nome, idade)) #Python 2
'''
nome = "JOSE"
idade = 33
salario = 987.3
print(f"O {nome} tem {idade} anos e ganha R${salario:.2f}")#normal
print(f"O {nome:^20} tem {idade} anos e ganha R${salario:.2f}")#centralizado sem traços
print(f"O {nome:->20} tem {idade} anos e ganha R${salario:.2f}")#a direita com traços
print(f"O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}")#a esquerda com traços
print(f"O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}") #centralizado com traços