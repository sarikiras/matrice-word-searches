from check_line import *
from diagonale import *

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

# je crée une nouvelle grille
new_grid = grid.copy()


def upper_check_line_1w(ligne, mot):
    # ligne peut eventuellement contenir des majuscules
    n = len(mot)
    if len(mot) <= len(ligne):
        ligne_temp = [i.lower() for i in ligne]
        for i in range(len(ligne_temp)-n+1):
            subset = ''.join(ligne_temp[i: i+n])
            if subset == mot or subset == mot[::-1]:
                for k in range(n):
                    ligne[i+k] = ligne[i+k].upper()
                return ligne


def upper_check_line(ligne, mots):
    mots_iter = mots.copy()
    for mot in mots_iter:
        result = upper_check_line_1w(ligne, mot)
        if result is not None:
            ligne = result
            mots.remove(mot)
    return ligne, mots


def check_grid_lines(grid, mots):
    new_grid = list(range(len(grid)))
    for i in range(len(grid)):
        ligne, mots = upper_check_line(grid[i], mots)
        new_grid[i] = ligne
    return new_grid, mots


def t_grid(grid):
    t_grid = []
    for j in range(len(grid[0])):
        col = []
        for i in grid:
            col.append(i[j])
        t_grid.append(col)
    return t_grid


def concatenation(grid):
    for ligne in grid:
        ligne = ''.join(ligne)
        print(ligne)


def check_grid_upper(grid, mots):

    grille_ini = [liste for liste in grid]

    check_grid_lines(grid, mots)
    check_grid_lines(t_grid(grid), mots)
    grid = t_grid(grid)
    # print(mots)
    for ligne in diagonales_GD(grille_ini):
        mots = check_line(ligne, mots)
    # print(mots)
    for ligne in diagonales_DG(grille_ini):
        mots = check_line(ligne, mots)
    # print(mots)
    for mot in mots:
        print(mot)
    return grid


if __name__ == '__main__':

    check_grid(grid, hidden_words)

#     for mot in mots:
#         print(mot)

# print(grid[-3], hidden_words[6])
# print(upper_check_line(grid[-3], ['raikou', 'tou', 'pipi']))
