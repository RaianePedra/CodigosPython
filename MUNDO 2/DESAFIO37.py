num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para a conversão."
      "\n\033[31m[ 1 ] \033[mBinário"
      "\n\033[31m[ 2 ] \033[mOctal"
      "\n\033[31m[ 3 ] \033[mHexadecimal")
resp = int(input("Insira a opção desejada: "))
if resp == 1:
    print("{} convertido para binário é igual a {}".format(num, bin(num)[2:]))
elif resp == 2:
    print("{} convertido para octal é igual a {}".format(num, oct(num)[2:]))
elif resp == 3:
    print("{} convertido para hexadecimal é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")