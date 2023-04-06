from check_line import *
from diagonale import *


def t_grid(grid):
    t_grid = []
    try:
        for j in range(len(grid)):      # cas où n=p
            col = []
            for i in grid:
                col.append(i[j])
        t_grid.append(col)
    except IndexError:
        raise IndexError(len(grid), len(grid[0]))
    return t_grid


def check_grid(grid, mots):
    for ligne in grid:
        mots = check_line(ligne, mots)
    for ligne in t_grid(grid):
        mots = check_line(ligne, mots)
    for ligne in diagonales_GD(grid):
        mots = check_line(ligne, mots)
    for ligne in diagonales_DG(grid):
        mots = check_line(ligne, mots)
    print(mots)


if __name__ == '__main__':
    liste = open('words.dic').read()
    mots = liste.split('\n')

    grille = open('grid').read()
    rows = grille.split('\n')
    grid = []
    for row in rows:
        ligne = []
        for lettre in row:
            ligne.append(lettre)
        grid.append(ligne)

    check_grid(grid, mots)
