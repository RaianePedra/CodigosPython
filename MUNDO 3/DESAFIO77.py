palavras = ("python", "amor", "programar", "linguagem", "curso",
            "trabalhar", "foco", "estudar", "praticar", "futuro")
print("-" * 30)
print(f'\033[33m{"Encontrando as vogais":^30}\033[m')
print("-" * 30)

for p in palavras:
    print(f"\nNa palavra \033[32m{p.upper()}\033[m temos ", end="")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f"\033[31m{letra}\033[m", end=' ')