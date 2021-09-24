frase = "Curso em video Python"
print(frase[3])#so a letra da cadeia 3
print(frase[3:13]) #Pegar do 3 ao 13(12)
print(frase[:13])#tudo que tinha antes do 13(12)
print(frase[13:])#tudo que tem depois do 13
print(frase[1:15:2])#do 1 ao 15 pulando de dois em dois
print(frase[::2])#do 0 ate o fim pulando de dois em dois
print(frase.count("o"))#conta quantos o (minusculo) tem
print(frase.upper().count("O"))#pega a frase joga pra maiuscula e conta as quantidades de "o"
print(len(frase))#Tamanho da frase
print(len(frase.strip()))#Tamanho da frase sem espaço
print(frase.replace("Python", "android"))#Trocar as palavras
print("Curso" in frase)#mostrar se é falso ou verdadeiro que esta na frase
print(frase.find("Curso"))#Mostra a posicao da palavra
print(frase.lower().find("video"))#acha um video minusculo em uma frase toda minuscula
print(frase.split())#cria listas com separador de espaco
dividido = frase.split()
print(dividido[0])#primeiro item da lista
print(dividido[2][3])#Item 2 da lista e mostrar a letra 3



'''print("""kjaisffijjdaflkdafkakfjkjfkjajkfjkjl
         kafkljkjdkfjakjfkjfkfdkfkaklf
         allfdkkndjnfam  
         kafjkakkeka """)#tres parenteses para texto
'''