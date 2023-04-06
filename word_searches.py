from check_line import *
from diagonale import *
from check_grid import *

liste = open('words.dic').read()
mots = liste.split('\n')
# print(mots)

grille = open('grid').read()
rows = grille.split('\n')
grid = []

for row in rows:
    ligne = []
    for lettre in row:
        ligne.append(lettre)
    grid.append(ligne)

if len(grid) == 0:
    raise IndexError('Grille vide ou non lue')
else:
    check_grid(grid, mots)
