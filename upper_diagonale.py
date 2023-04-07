from diagonale import grid_inf, grid_sup
from upper_grid import *
from reconstitution import *


# Cas où j'ai une grille carrée de taille n
def upper_diagonales_GD(grid, mots):

    n = len(grid)

    Grid_sup = grid_sup(grid, n)
    upper_Grid_sup, mots = check_grid_lines(Grid_sup, mots)
    triang_sup = join_grid_sup(upper_Grid_sup)

    Grid_inf = grid_inf(grid, n)
    upper_Grid_inf, mots = check_grid_lines(Grid_inf, mots)
    triang_inf = join_grid_inf(upper_Grid_inf)
    join_grid = rassemblement(triang_inf, triang_sup)

    diagonale = [grid[i][i] for i in range(n)]
    diag, mots = upper_check_line(diagonale, mots)
    for i in range(n):
        join_grid[i][i] = diag[i]

    return join_grid


if __name__ == '__main__':

    liste = open('words.dic').read()
    mots = liste.split('\n')
    mots.pop()

    grille = open('grid').read()
    rows = grille.split('\n')
    rows.pop()
    grid = []
    for row in rows:
        ligne = []
        for lettre in row:
            ligne.append(lettre)
        grid.append(ligne)

    pfiou = upper_diagonales_GD(grid, mots)
    concatenation(pfiou)
