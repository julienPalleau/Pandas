# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7856832-creez-vos-premiers-arrays-avec-numpy

import numpy as np

revenus = [1800, 1500, 2200, 3000, 2172]
x = [-2, -1, 1, 2]
print("La valeur absolue: ", np.abs(x))
print("Exponentielle: ", np.exp(x))
print("Logarithme: ", np.log(np.abs(x)))
# Il en existe de nombreuses autres: https://docs.scipy.org/doc/numpy-1.13.0/reference/ufuncs.html

# Creation d'un array Numpy
revenus_array = np.array(revenus)
print(f"array revenus: {revenus_array}")

# Acces à un element specifique d'un array se fait via la syntaxe: nom_array[indice]:
# Pour acceder au 5eme element
print(f"Acces au 5eme element revenus_array[4]: {revenus_array[4]}")

# pour acceder au dernier element
print(f"Acces au dernier element revenus_array[-1]: {revenus_array[-1]}")

# On peut aussi modifier les valeurs
revenus_array[1] = 1900

# exercice sur le tableau suivant revenus = [1800, 1500, 2200, 3000, 2172]
print("\n")
print(f"exercice sur le tableau suivant, revenus = [1800, 1500, 2200, 3000, 2172]")

# Accedez à plusieurs elements contigus
print(f"Accedez à plusieurs elements contigus revenus_array[0:3]: {revenus_array[0:3]}")

# Les 3 premiers elements
print(f"Les 3 premiers elements revenus_array[:3]: {revenus_array[:3]}")

# Les elements à partir de l'indice 2
print(f"Les elements à partir de l'indice 2 revenus_array[2:]: {revenus_array[2:]}")

# Un element sur 2
print(f"Un element sur 2 revenus_array[::2]: {revenus_array[::2]}")

# Inverser le contenu de l'array
print(f"Ordre invers revenus_array[::-1]: {revenus_array[::-1]}")

# Accedez à plusieurs elements selon une condition
print(f"Voilà par exemple comment sélectionner uniquement les valeurs supérieures à 2 000 € revenus_array[revenus_array > 2000]: {revenus_array[revenus_array > 2000]}")

# Nous pouvons complexifier les conditions
print(f"Il est possible de complexifier les conditions revenus_array[(revenus_array > 2000) & (revenus_array < 3000)]: {revenus_array[(revenus_array > 2000) & (revenus_array < 3000)]}")

# Utilisation des methodes d'array: .dtype, .dshape
print("\n")
print(f"Dimension de l'array avec revenus_array.shape: {revenus_array.shape}")

# Calcul de la moyenne
print(f"calcul de la moyenne: {revenus_array.mean()}")

# Calculer le maximum (ou le minimum):
print(f"exercice sur le tableau suivant, revenus: {revenus_array}")
print(f"calcul le maximum: {revenus_array.max()}")
print(f"Calcul le minimum: {revenus_array.min()}")

# Acceder à l'indice de l'element minimum (ou maximum):
print(f"Indice de l'element minimum revenus_array.argmin(): {revenus_array.argmin()}")
print(f"Indice de l'element maximumu revenus_array.argmax(): {revenus_array.argmax()}")

# Orodonner par ordre croissant:
revenus_array.sort()
print(f"Orodonner par ordre croissant revenus_array.sort(): {revenus_array}")

# Calculer la somme:
print(f"Calculer la somme revenus_array.sum(): {revenus_array.sum()}")

# La liste n'est pas exaustives plus d'info @ https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html

# Exercice
print("\n\n")
print(""" Exercice 1: \n
Créez vos premiers arrays avec Numpy

Tout au long de ce cours, nous allons nous mettre dans la peau d’une personne travaillant dans un service data au sein d'une banque. Plus précisément, vous travaillez pour la 
filière gérant les différents prêts. L’objectif sera d’utiliser les connaissances acquises sur les librairies Python pour aider l’agence dans différentes tâches.

Pour cette première tâche, nous avons à notre disposition les revenus de 10 clients de notre banque. Vous aurez à utiliser les différentes manipulations présentées dans ce 
chapitre pour sélectionner certains revenus selon une condition spécifique et effectuer diverses opérations.""")
print("\n")
liste = [1800, 1500, 2200, 3000, 2172, 50000, 1400, 1200, 1100, 1300]
revenus = np.array(liste)
haut_revenus = revenus[revenus > 3000]
print(f"haut revenus: {haut_revenus}")
print("\n")
print(f"Somme des revenus annuelles: {round((revenus.sum()*12) / 1_000_000, 2)}, M€")
print(f"moyenne des revenus des 10 clients: {revenus.mean()} €")


revenus[revenus == 1400] = 1600
print(f"Salaire apres augmentation: {revenus[revenus==1600]}")
# ou
# np.where(revenus == 1400) retourne une liste d'index auxquelles on trouve 1400, tandis que np.where(revenus == 1400)[0][0] retourne le premier index ou l'on trouve 1400
# indice = np.where(revenus == 1400)[0][0]
# revenus[indice] += 200
# print(revenus[indice])

#############
# En resume #
#############
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7856832-creez-vos-premiers-arrays-avec-numpy#/id/r-7856831
"""
    NumPy (pour Numerical Python) est une librairie Python permettant de manipuler et d’effectuer rapidement et simplement de nombreuses opérations mathématiques sur un tableau 
    de données.

    Les données sont stockées dans une structure similaire à une liste Python, un tableau NumPy, ou array.

    Ce dernier, contrairement à une liste, est obligatoirement monotype.

    On peut sélectionner au sein d’un array :

        un élément via son indice avec l’écriture :  nom_array[indice]  ;

        plusieurs éléments contigus via la syntaxe :  nom_array[début:fin:pas]  ;

        certains éléments spécifiques via une condition :  nom_array[condition]  .

    Les arrays possèdent de nombreuses méthodes permettant de les manipuler ou d'effectuer des opérations mathématiques, de façon très simple.
"""