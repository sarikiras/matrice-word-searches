# je crée la liste des diagonales lues de gauche à droite

# fonction qui liste les diagonales inférieures
# d'une matrice carrée de taille n (sans la diagonale principale)

def grid_inf(grid, n):                      # good!
    liste = []
    for k in range(1, n):
        ligne = []
        for j in range(n-k):
            ligne.append(grid[j+k][j])
        liste.append(ligne)
    return liste


# fonction qui liste les diagonales inférieures
# d'une matrice carrée de taille n (sans la diagonale principale)

def grid_sup(grid, n):              # very good!
    liste = []
    for k in range(1, n):
        ligne = []
        for i in range(n-k):
            ligne.append(grid[i][i+k])
        liste.append(ligne)
    return liste


def diagonales_GD(grid):            # excellent!

    n = len(grid)
    p = len(grid[0])
    d = abs(n-p)

    liste = [[grid[i][i] for i in range(min(n, p))]]

    # je crée la liste des diagonales, cas où n ≤= p

    if len(grid) < len(grid[0]):

        # je crée la liste des diagonales inférieures
        # similaire au cas où n=p

        liste += grid_inf(grid, n)

        # je crée la liste des diagonales supérieures dans ce cas

        # d'abord la bande centrale
        for k in range(1, d+1):
            ligne = []
            for i in range(n):
                ligne.append(grid[i][i+k])
            liste.append(ligne)

        # puis les diagonales supérieures
        new_grid = list(range(n))
        for i in range(n):
            new_grid[i] = grid[i][d:]

        liste += grid_sup(new_grid, n)

        return liste

    if len(grid) >= len(grid[0]):                # n > p

        # je crée la liste des diagonales supérieures dans ce cas
        # même cas que n = p

        liste += grid_sup(grid, p)

        # je crée la liste des diagonales inférieures
        # d'abord la bande centrale
        for k in range(1, d+1):
            ligne = []
            for j in range(p):
                ligne.append(grid[j+k][j])
            liste.append(ligne)

        # puis je rajoute les diagonales inférieures
        new_grid = list(range(p))
        for i in range(p):
            new_grid[i] = grid[i+d]
        liste += grid_inf(new_grid, n)

        return liste


# je crée la liste des diagonales lues de droite à gauche

def diagonales_DG(grid):
    # je crée la grid miroir
    grid_mir = [i[::-1] for i in grid]
    return diagonales_GD(grid_mir)


if __name__ == '__main__':

    grille = open('grid_test').read()
    rows = grille.split('\n')
    rows.pop()
    grid = []
    for row in rows:
        ligne = []
        for lettre in row:
            ligne.append(lettre)
        grid.append(ligne)

    # print(diagonales_DG(grid))

    print(diagonales_GD(grid))
