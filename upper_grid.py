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
new_grid = [i for i in grid]


def upper_check_line_1w(ligne, mot):
    # je définis une fonction qui renvoie une ligne si elle est modifiée
    # ligne peut déjà eventuellement contenir des majuscules
    n = len(mot)
    if len(mot) <= len(ligne):
        ligne_temp = [i.lower() for i in ligne]
        for i in range(len(ligne_temp)-n+1):
            subset = ''.join(ligne_temp[i: i+n])
            if subset == mot or subset == mot[::-1]:
                for k in range(n):
                    ligne[i+k] = ligne[i+k].upper()
                return ligne


def upper_check_line(ligne, mots):  # ici c'est la ligne initiale en minuscules
    # cette fonction renvoie la ligne modifiée
    mots_iter = [mot for mot in mots]
    for mot in mots_iter:
        result = upper_check_line_1w(ligne, mot)
        if result is not None:
            ligne = result
            mots.remove(mot)
    return ligne, mots


def check_grid_lines(grid, mots):
    # cette fonction me renvoie toute la grille modifiée
    new_grid = []
    for ligne in grid:
        new_ligne, mots = upper_check_line(ligne, mots)
        new_grid.append(new_ligne)
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

    new_grid, mots = check_grid_lines(grid, mots)  # modif lignes
    new_grid, mots = check_grid_lines(t_grid(new_g rid), mots)  # id colonnes
    new_grid = t_grid(new_grid)
    for ligne in diagonales_GD(grid):
        mots = check_line(ligne, mots)
    for ligne in diagonales_DG(grid):
        mots = check_line(ligne, mots)
    for mot in mots:
        print(mot)
    return new_grid


if __name__ == '__main__':

    check_grid_upper(grid, hidden_words)
    # print(upper_check_line(grid[-1], ['oups', 'coucou', 'papa']))
