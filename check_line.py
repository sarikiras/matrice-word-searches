# check_line(ligne, mot) est une fonction qui vérifie
# si le mot est dans la ligne, dans les 2 sens

def check_line_1w(ligne, mot):
    n = len(mot)
    subset_n = []
    for i in range(len(ligne)-n+1):
        subset = ''.join(ligne[i: i+n])
        subset_n.append(subset)
        subset_n.append(subset)
    subset_n_rvse = [mot[::-1] for mot in subset_n]
    return mot in subset_n or mot in subset_n_rvse


def check_line(ligne, mots):
    for mot in mots:
        if check_line_1w(ligne, mot):
            mots.remove(mot)
    return mots


def check_grid(grid, mots):
    for ligne in grid:
        check_line(ligne, mots)
    return mots


if __name__ == '__main__':
    ligne = ['h', 'h', 'c', 'h', 'a', 'r', 'i', 'z', 'a', 'r',
             'd', 's', 'o', 'i']
    mot = 'charizard'
    print(check_line_1w(ligne, mot))

    liste = open('words.dic').read()
    mots = liste.split('\n')
    print(check_line(ligne, mots))
