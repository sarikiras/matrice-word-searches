from upper_grid import concatenation, t_grid


def join_grid_sup(split_grid_sup):
    n = len(split_grid_sup) + 1
    new_grid = []
    for i in range(n):
        ligne = []
        for _ in range(i+1):
            ligne.append('0')
        for k in range(n-1-i):
            ligne.append(split_grid_sup[k][i])
        new_grid.append(ligne)
    return new_grid


def join_grid_inf(split_grid_inf):
    new_grid = t_grid(join_grid_sup(split_grid_inf))
    return new_grid


def rassemblement(grid_inf, grid_sup):

    n = len(grid_inf)
    new_grid = [['' for i in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i <= j:
                new_grid[i][j] = grid_sup[i][j]
            else:
                new_grid[i][j] = grid_inf[i][j]
    return new_grid


if __name__ == '__main__':

    triang = [['1', '2', '3'], ['4', '5'], ['6']]
    grille = rassemblement(join_grid_inf(triang), join_grid_sup(triang))
    print(grille)
    concatenation(grille)
