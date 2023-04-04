from check_line import *

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

t_grid = []

print(check_grid(grid, mots))
