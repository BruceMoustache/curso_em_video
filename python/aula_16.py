lanches = 'Hamburguer', 'Pizza', 'Cenoura', 'Batata frita', 'Cenoura'

for comida in lanches:
    print(f'Eu vou comer {comida}')

for contador in range(len(lanches)):
    print(f'Eu vou comer {lanches[contador]} em posicao {contador}')

for posicao, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posicao {posicao}')

print('Comi para caramba')

print(sorted(lanches))
print(lanches.index('Pizza'))
print(lanches.count('Cenoura'))

