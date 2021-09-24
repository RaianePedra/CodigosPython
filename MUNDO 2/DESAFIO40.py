nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

print("Tirando {:.1f} e {:.1f}, a média do aluno é: \033[30m{:.1f}\033[m".format(nota1, nota2, media))

if media <= 5.0:
    print("\033[31mREPROVADO.\033[m")
elif media >= 7.0:
    print("\033[34mPARABÉNS, VOCÊ FOI APROVADO!!!\033[m")
else:
    print("\033[33mRECUPERAÇÃO\033[m")
