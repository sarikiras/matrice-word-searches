# check_line(ligne, mot) est une fonction qui vérifie
# si le mot est dans la ligne, dans les 2 sens
# from upper_grid import*

def check_line_1w(ligne, mot):
    n = len(mot)
    if len(mot) <= len(ligne):
        subset_n = []
        for i in range(len(ligne)-n+1):
            subset = ''.join(ligne[i: i+n])
            subset_n.append(subset)
        # print(subset_n)
        # subset_n_rvse = [mot[::-1] for mot in subset_n]
        # print(subset_n_rvse)
        inv_mot = mot[::-1]
        return mot in subset_n or inv_mot in subset_n


def check_line(ligne, mots):
    for mot in mots:
        if check_line_1w(ligne, mot):
            mots.remove(mot)
    return mots


if __name__ == '__main__':
    ligne = ['h', 'h', 'c', 'h', 'a', 'r', 'i', 'z', 'a', 'r',
             'd', 's', 'o', 'i']
    mot = 'charizard'
    print(check_line_1w(ligne, mot))

    liste = open('words2.dic').read()
    mots = liste.split('\n')
    print(check_line(ligne, mots))
