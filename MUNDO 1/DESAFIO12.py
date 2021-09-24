preço = float(input("Preço do produto: "))

desc = preço - (preço * 5 / 100)

print("O preço do produto com desconto será: {}".format(desc))