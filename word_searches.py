from check_line import *
from diagonale import *
from check_grid import *

liste = open('words.dic').read()
mots = liste.split('\n')
hidden_words = []
for mot in mots:
    if mot != '':
        hidden_words.append(mot)
# print(hidden_words)

grille = open('grid').read()
rows = grille.split('\n')
rows.pop()
# print(rows)
grid = []

for row in rows:
    ligne = []
    for lettre in row:
        ligne.append(lettre)
    grid.append(ligne)

check_grid(grid, mots)
