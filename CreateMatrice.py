tableau =    [0, 0, 0, 0, 0, 26, 27, 27, 38, 30,
            6, 7, 8, 0, 0, 29, 22, 27, 30, 46,
            14, 15, 16, 0, 0, 29, 38, 35, 22, 27,
            22, 23, 24, 0, 0, 26, 27, 38, 30, 27,
            30, 31, 32, 0, 0, 34, 35, 38, 43, 43,
            38, 39, 40, 0, 0, 42, 43, 38, 43, 22,
            46, 47, 48, 0, 0, 37, 46, 46, 46, 38,
            54, 55, 56, 0, 0, 26, 27, 30, 27, 27,
            62, 63, 64, 0, 0, 34, 35, 27, 38, 30,
            0, 0, 0, 0, 0, 42, 43, 35, 30, 30]

         
         


def transformer_en_tableau_2D(tableau_simple, nombre_colonnes):
    tableau_2D = [tableau_simple[i:i+nombre_colonnes] for i in range(0, len(tableau_simple), nombre_colonnes)]
    return tableau_2D

nombre_colonnes = 10

tableau_2D = transformer_en_tableau_2D(tableau, nombre_colonnes)

def ajouter_accolade_et_virgule(tableau_2D):
    for i in range(len(tableau_2D)):
        if i == 0:
            tableau_2D[i] = "{" + str(tableau_2D[i])[1:-1] + "},"
        elif i == len(tableau_2D) - 1:
            tableau_2D[i] = "{" + str(tableau_2D[i])[1:-1] + "},"
        else:
            tableau_2D[i] = "{" + str(tableau_2D[i])[1:-1] + "},"

ajouter_accolade_et_virgule(tableau_2D)

for ligne in tableau_2D:
    print(ligne)
