# 2. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feito em cada partida. No final tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gol_por_partida = []
jogador['nome'] = input('Digite o nome do jogador: ')
total = int(input('Digite o total de partidas jogadas: '))
for i in range(total):
    gol_por_partida.append(int(input(f'Digite a quantidade de gols na partida {i+1}: ')))
jogador['gols'] = gol_por_partida[:]
jogador['total'] = sum(gol_por_partida)

print('*-=-*'*10)
print('Nome do jogador:', jogador['nome'])
print('*-=-*'*10)
print(f"o jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
print('*-=-*'*10)

for k,v in enumerate(jogador['gols']):
    print(f'\t- Na partida {k+1} ele fez {v} gols!')
print('*-=-*'*10)
print(f"O {jogador['nome']} fez {jogador['total']} gols no campeonato, com média de {jogador['total']/len(jogador['gols'])} gols por partida! ")








