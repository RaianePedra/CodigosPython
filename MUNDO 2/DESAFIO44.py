print("\033[33m{:=^40}".format(" CALCULO DO PRODUTO "))
prec = float(input("\033[30mInsira o preço do produto: R$\033[m"))
print("\n\033[32mTABELA DE PREÇO\033[m")
print("\033[32m1-\033[m À vista com dinheiro/cheque: 10% de desconto\n\033[32m2-\033[m À vista com cartão: 5% de desconto\n\033[32m3-\033[m 2x no cartão: Preço normal\n\033[32m4-\033[m 3x ou mais no cartão: 20% de juros")
esc = int(input("\033[30mInsira a opção desejada: \033[m"))
if esc == 1:
    total = prec - (prec * 0.10)
elif esc == 2:
    total = prec - (prec * 0.05)
elif esc == 3:
    total = prec
    parcela = total/2
    print("Sua compra será parcelada em 2x de \033[33m{:.2f}R$\033[m".format(parcela))
elif esc == 4:
    total = prec + (prec * 0.20)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print("\033[32mSua compra será parcelada em {}x de R${:.2f} com juros.\033[m".format(totparc, parcela))
else:
    total = prec
    print("\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!\033[m")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(prec, total))
