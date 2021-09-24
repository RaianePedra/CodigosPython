times = ("Internacional", "São Paulo", "Vasco da Gama", "Fluminense", "Flamengo",
         "Ceará SC", "Palmeiras", "Atlético-MG", "Corinthians", "Fortaleza",
         "Santos", "Bahia", "Atlético-PR", "Coritiba", "Grêmio",
         "Botafogo", "Bragantino-SP", "Atlético-GO", "Goiás", "Sport Recife")
print("-=" * 15)
print(f'Lista de times: {times}')
print("-=" * 15)
print(f'Os 5 primeiros sao:{times[0:5]}')  12
print("-=" * 15)
print(f'Os 4 ultimos sao:{times[-4:]}')
print("-=" * 15)
print(f'Os times em ordem alfabetica sao:{sorted(times)}')
print("-=" * 15)
print(f'O Santos está na {times.index("Santos") + 1}ª posição.')
