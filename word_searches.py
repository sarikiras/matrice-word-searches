from check_line import *
from diagonale import *
from check_grid import *
from upper_grid import *


liste = open('words_test.dic').read()
mots = liste.split('\n')
hidden_words = []
for mot in mots:
    if mot != '':
        hidden_words.append(mot)
# print(hidden_words)

grille = open('grid_test').read()
rows = grille.split('\n')
rows.pop()
# print(rows)
grid = []

for row in rows:
    ligne = []
    for lettre in row:
        ligne.append(lettre)
    grid.append(ligne)

check_grid(grid, hidden_words)
# concatenation(grid)
