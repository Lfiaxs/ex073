tabela = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo',
          'Cruzeiro', 'São Paulo', 'Bahia', 'Vasco da Gama',
          'Atlético - MG', 'Internacional', 'Bragantino', 'Athletico - PR',
          'Juventude', 'Criciúma', 'Grêmio', 'Fluminense',
          'Corinthians', 'Vitória', 'Cuiabá', 'Atlético - GO')
print('-='*15)
print(f'Lista de times do Brasileirão: {tabela}')
print('-='*15)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('-='*15)
print(f'Os últimos 4 são: {tabela[-4:]}')
print('-='*15)
print(f'Os times em lista alfabética são: {sorted(tabela)}')
print('-='*15)
print(f'O Criciúma está na {tabela.index("Criciúma")+1}ª posição.')

