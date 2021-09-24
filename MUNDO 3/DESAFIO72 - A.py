"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

contagem = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
            "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
print("\033[33mObs: Se outro número for digitado irá sair do programa.\033[m")
while True:
    num = int(input("Insira um número entre 0 e 20:"))
    if num < 0 or num > 20:
        break
    print(f"Você digitou o número \033[34m{contagem[num]}\033[m")

    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("\033[31mFim do programa.\033[m")
