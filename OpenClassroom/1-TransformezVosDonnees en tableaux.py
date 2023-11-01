# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux

import numpy as np

# Transformez vos donnees en tableaux

##############################
# Creez un tableu avec NumPy #
##############################

# un tableau de 3x5 rempli de 1
print(f"un tableau de 3x5 rempli de 1 np.ones((3, 5)): \n{np.ones((3, 5))}")

# un tableau de 4 lignes et de 4 colonnes contenant que des 0
print(f"un tableau de 4 lignes et de 4 colonnes contenant que des 0 np.zeros((4, 4)): \n{np.zeros((4, 4))}")

# un tableau de # un tableau de 6x3 rempli de valeurs aléatoires comprises entre 0 et 1
print(f"un tableau de 6x3 rempli de valeurs aléatoires comprises entre 0 et 1 np.random.random((6, 3)): \n{np.random.random((6, 3))}")

# un tableau de 3x3 rempli de valeurs aléatoires entières, comprises entre 1 et 10
print(f"un tableau de 3x3 rempli de valeurs aléatoires entières, comprises entre 1 et 10 np.random.randint(1, 10, size=(3, 3)): \n{np.random.randint(1, 10, size=(3, 3))}")

#########################################################
# Decouvrez l'analogie entre les arrays et les matrices #
#########################################################
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux#/id/r-7856976

################################################
# Maitrisez les manipulations avancees d'array #
################################################
hugo = [1300, 400, 23]
richard = [1700, 560, 24]
emilie = [2500, 900, 30]
gaspard = [3000, 1000, 22]
yohann = [2400, 700, 28]
chloe = [3000, 700, 34]
matthieu = [3500, 900, 35]
luc = [4000, 1200, 33]
rachel = [3300, 950, 27]
maude = [1850, 600, 25]

tableau = [hugo, richard, emilie, gaspard, yohann, chloe, matthieu, luc, rachel, maude]
print(tableau)
# Array manipulation routines: https://numpy.org/doc/stable/reference/routines.array-manipulation.html

print("\n")
print("Exercice 2:\n")
hugo = [1800, 21, 0]
richard = [1500, 54, 2]
emilie = [2200, 28, 3]
pierre = [3000, 37, 1]
paul = [2172, 37, 2]
deborah = [5000, 32, 0]
yohann = [1400, 23, 0]
anne = [1200, 25, 1]
thibault = [1100, 19, 0]
emmanuel = [1300, 31, 2]

tableau = [hugo, richard, emilie, pierre, paul, deborah,
           yohann, anne, thibault, emmanuel]

print(f"tableau: {tableau}")

"""
Paul souhaiterait contracter un prêt immobilier :

    affichez les informations qui lui sont relatives. Pour rappel, Paul correspond à la 5ème ligne de nos données
    calculez ses mensualités maximales, en sachant que le taux d'endettement maximum est de 35% (il ne pourra donc pas rembourser par mois plus de 35% de son revenu).
"""
print("\n")
data = np.array(tableau)
print("Informations de Paul :")
print(data[4, :])
print("-")
print(f"Ses mensualités maximales sont de : {round((data[4][0]*35)/100,2)} €")

"""
Un nouveau client vient d'arriver, dont les informations sont les suivantes : 
louise = [1900, 31, 1]
"""
louise = [1900, 31, 1]
print("\n")
data = np.vstack((data, louise))
print(data)

print("---\n")
revenus = data[:, 0]
print(revenus)