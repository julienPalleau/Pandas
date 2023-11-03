# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux

#######################################
# Transformez vos donnees en tableaux #
#######################################

###############################
# Creez un tableau avec NumPy #
###############################
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux#/id/r-7856948

"""
Jusque-là, nous n’avons vu que des tableaux/arrays à une dimension, mais on ne travaille que très rarement avec une seule colonne.

Prenons un exemple : vous travaillez dans le milieu bancaire et vous avez besoin de créer un tableau où vous retrouveriez, en plus des revenus de vos clients, leurs mensualités de
remboursement de prêt, le nombre d'enfants à charge, et toute autre information susceptible de vous être utile.

Considérons les clients suivants :
    + Hugo, un jeune homme de 21 ans, gagnant 1 400 € par mois et n’ayant aucun enfant ;
    + Richard, un homme de 54 ans, gagnant 2800 € par mois et ayant 2 enfants ;
    + Émilie, une femme de 27 ans gagnant 3 700 € et ayant 3 enfants.

Nos données peuvent être représentées via ce tableau :
            Age Revenus Nombre d'enfants
Hugo        21  1400    0
Richard     54  2800    2
Emilie      27  3700    3

Et voici comment pourrait se matérialiser ce tableau en Python, en utilisant des listes :
hugo = [21, 1400, 0]
richard = [54, 2800, 2]
emilie = [27, 3700, 3]

tableau = [hugo, richard, emilie]

Décortiquons cela ensemble :
    + Dans un premier temps, nous créons une liste pour chaque personne dans notre banque, contenant l’ensemble des informations à disposition sur cette personne ;
    + Enfin, nous créons une liste  tableau  dans laquelle nous stockons l’ensemble des différentes listes créées précédemment.

La listetableau contient donc 3 éléments, qui sont eux-mêmes des listes de 3 éléments : c’est donc une liste de listes. Nous avons néanmoins toujours l’ensemble des limitations
liées aux listes, avec cette façon de faire.

Comment pourrions-nous faire alors ?

Vous vous en doutez très certainement, mais oui, encore une fois la réponse se trouve du côté de NumPy et des arrays !

En effet, un array est un objet multidimensionnel, c’est-à -dire qu’il est possible de créer des arrays de toutes dimensions, et que l’ensemble des méthodes d’array prennent en
compte ce côté multidimensionnel. Génial, non ? Testons tout cela ensemble !

La façon la plus simple de créer un tableau est de le faire à partir d’une liste de listes Python, comme avec une liste classique. Il suffira d'exécuter np.array(tableau) pour
transformer notre liste de listes en array NumPy de 3 lignes et 3 colonnes.

Voyons quelques autres exemples ensemble pour bien comprendre cette notion :

tab1 = np.array([[1, 2],
    [3, 4],
    [5, 6]])

tab2 = np.array([[1, 2, 3],
        [4, 5, 6]])

Ces quelques lignes de code permettent de créer :
    + un array  tab1  de 3 lignes et 2 colonnes ;
    + et un array  tab2  de 2 lignes et 3 colonnes.

Il est possible de créer des tableaux en bien plus que 2 dimensions. Par exemple, pour un tableau en 3D il suffira d’utiliser une liste de listes de listes.

Comme précédemment, nous pouvons également utiliser des fonctions NumPy pour créer des tableaux plus ou moins complexes. Voici quelques exemples de fonctions couramment utilisées :

# un tableau de 3x5 rempli de 1
np.ones((3, 5))

# un tableau de 4 lignes et de 4 colonnes contenant que des 0
np.zeros((4, 4))

# un tableau de 6x3 rempli de valeurs aléatoires comprises entre 0 et 1
np.random.random((6, 3))

# un tableau de 3x3 rempli de valeurs aléatoires entières, comprises entre 1 et 10
np.random.randint(1, 10, size=(3, 3))

N’hésitez pas à reprendre ces fonctions et à les exécuter dans votre propre environnement en changeant certaines valeurs, pour bien appréhender leur fonctionnement.

#########################################################
# Découvrez l’analogie entre les arrays et les matrices #
#########################################################
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux#/id/r-7856976
Vous vous souvenez que j’ai évoqué le fait que NumPy était une librairie Python dessinée pour les calculs scientifiques ? Les tableaux que nous avons vus ensemble jusqu'ici,
matérialisés par des arrays NumPy, portent le nom de matrices, en mathématiques. Le but premier de NumPy, avant même toutes ses applications dans le domaine de la data, est de
proposer des outils pour manipuler ces matrices et effectuer ce qu’on appelle des calculs matriciels.
Une matrice est un tableau d'éléments, comme nous avons pu en voir jusqu'ici. On a l’habitude de la représenter sous la forme suivante :
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux#/id/r-7862323
1 2 3
4 5 6
7 8 9

Les matrices sont une composante essentielle de l’algèbre linéaire. Vous allez forcément être amené à croiser à nouveau leur chemin si vous poursuivez dans l’analyse de données,
car elles sont la base même de nombreuses méthodes statistiques de modélisation !!

Nous avons régulièrement à effectuer différentes opérations avec ces matrices. Considérons les 3 matrices suivantes, A, B et C :
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux#/id/r-7862326

Comme elles sont de même dimension (même nombre de lignes et de colonnes), on peut calculer la somme (ou la différence) de la matrice A et de la matrice B, en additionnant terme à
terme chaque élément :
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux#/id/r-7862329

La même chose avec NumPy :

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 10], [15, 20]])
C = np.array([[2, 4, 6], [8, 10, 12]])
print(A+B)

Il est également possible de faire une multiplication terme à terme via l’opérateur  * , comme avec une multiplication normale : A*B .
Cependant, lorsqu’on effectue des calculs matriciels, on utilise beaucoup plus ce qu’on appelle le produit matriciel. C’est un calcul assez fastidieux à faire à la main –
d’autant plus avec des matrices de grande dimension – mais qu’un ordinateur n'a en revanche aucun problème à réaliser.

Le calcul matriciel est une notion un peu complexe. Si vous souhaitez approfondir cette notion ou simplement avoir une perspective différente, je vous dirige vers cette excellente
vidéo du produit matriciel qui couvre très bien la notion de façon visuelle !

Avec NumPy, le produit matriciel se fait via l’opérateur @  :  A @ C . Cependant, cet opérateur n’est disponible que depuis Python 3.5. Avant cela, le produit matriciel se faisait
via la fonction dot de NumPy :  AC = np.dot(A, C) . Cette dernière fonctionne toujours aujourd’hui, les deux syntaxes sont donc possibles !

################################################
# Maitrisez les manipulations avancees d'array #
################################################
Vous vous souvenez lorsque je vous ai dit que l’ensemble des méthodes d’array prenaient en compte l’aspect multidimensionnel des arrays ? Je vous propose d'approfondir cela
ensemble dans la vidéo suivante. Nous verrons notamment :
    + comment modifier un array existant ;
    + comment accéder aux différents éléments d’un array via leurs indices ;
    + quelques méthodes qui sauront se montrer utiles lors de calculs scientifiques.
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857032-transformez-vos-donnees-en-tableaux#/id/video_Player_1

Il existe naturellement bien d’autres méthodes implémentées ! Vous en trouverez la liste complète dans la documentation officielle de NumPy.

#############
# En Resume #
#############
+ Les arrays NumPy sont multidimensionnels, ils peuvent être en 2 dimensions pour correspondre aux besoins du format des données en data, voire en 3D ou 4D.
+ Il est possible de créer des tableaux NumPy :
    + via la fonction array de NumPy à partir de listes de listes Python :  np.array(liste_de_liste) ;
    + à partir des fonctions prédéfinies de NumPy pour remplir un tableau avec des valeurs aléatoires, ou avec une valeur fixe.

+ On peut accéder aux éléments d’un array A en utilisant la syntaxe  A[i, j] , où  i  et  j  sont respectivement le numéro de ligne et le numéro de colonne de l’élément au sein
du tableau. L’opérateur :  permet de sélectionner plusieurs éléments, voire tout une ligne ou colonne.
+ Il existe de nombreuses méthodes applicables à des arrays, dont la liste exhaustive se trouve sur la documentation officielle de NumPy.
+ Ces tableaux de valeurs numériques sont appelés des matrices, en mathématiques. De nombreux algorithmes font intervenir des calculs matriciels, et nécessitent l’utilisation de
NumPy lorsqu’ils sont écrits en Python.
"""