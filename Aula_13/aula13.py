
vingadores = {'Chris Evans':'Capitão América', 'Mark Ruffalo':'Hulk', 'Tom Hiddleston':'Loki', 'Chris Hemsworth':'Thor', 'Robert Downey Jr':'Homem de Ferro', 'Scarlet Johansson':'Viúva Negra'}

print(vingadores['Chris Evans'])
print(vingadores.get('Tom Hiddleston','Não encontrado'))
print('Hulk' in vingadores.values())

vingadores['Mike Myers'] = 'Austin Powers'
vingadores['Arnold Schwarzenegger'] = 'Terminator'
vingadores['Sylvester Stallone'] = 'Rambo'

print(vingadores)

del vingadores['Mike Myers']
 
print(vingadores)

vingadores['Mike Myers'] = 'Austin Powers'

print(vingadores)

print(vingadores.pop(input('Digite o nome do ator: '),'Ator não encontrado'))

animais = {'Cão':'Vira-Lata', 'Cavalo':'Mangalarga', 'Gato':'Siamês'}

for i in animais:
    vingadores[i] = animais[i]
    
print(vingadores)