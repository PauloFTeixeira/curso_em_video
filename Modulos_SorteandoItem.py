"""
Sorteando um item de uma lista de nomes
Sorteando uma ordem na liste de nomes

"""
import random

nomes = ['Paulo', 'Eduarda', 'Habner', 'Gabriel']

#  Escolhendo um nome específico
escolhido = random.choice(nomes)
print(escolhido)

# Escolhendo uma ordem de nomes
random.shuffle(nomes)
print(nomes)

