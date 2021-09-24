import emoji
from time import sleep
print("\033[33mVamos iniciar a contagem regressiva para os fogos!!!\033[m")
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize("\033[33mVIVA!!! :boom::collision:\033[m", use_aliases=True))