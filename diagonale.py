# je crée la liste des diagonales lues de gauche à droite
def diagonales_GD(grid):

    liste = [[grid[i][i] for i in range(len(grid))]]
    for k in range(1, len(grid)):

        # je crée la liste des diagonales inférieures, cas où n=p
        ligne = []
        for j in range(len(grid) - k):
            ligne.append(grid[j+k][j])
        liste.append(ligne)

        # je crée la liste des diagonales supérieures, cas où n=p
        ligne = []
        for i in range(len(grid) - k):
            ligne.append(grid[i][i+k])
        liste.append(ligne)

    return liste


# je crée la liste des diagonales lues de droite à gauche

def diagonales_DG(grid):

    liste = [[grid[i][-i-1] for i in range(len(grid))]]
    for k in range(1, len(grid)):

        # je crée la liste des diagonales inférieures, cas où n=p
        ligne = []
        for i in range(k, len(grid)):
            ligne.append(grid[i][-i-1+k])
        liste.append(ligne)

        # je crée la liste des diagonales supérieures, cas où n=p
        ligne = []
        for i in range(len(grid)-k):
            ligne.append(grid[i][-i-1-k])
        liste.append(ligne)

    return liste


if __name__ == '__main__':

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
    print(diagonales_DG(grid))
