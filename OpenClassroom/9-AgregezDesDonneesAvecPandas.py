# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857733-agregez-des-donnees-avec-pandas

###################################
# Agregez des donnees avec Pandas #
###################################
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857733-agregez-des-donnees-avec-pandas#/id/r-7859277
"""
Maintenant que nous sommes capables d’accéder à tout ce que nous souhaitons au sein de notre data frame, je vous propose de voir comment agréger les différentes informations.
Notre banque opère dans 6 villes différentes : Toulouse, Paris, Marseille, Lyon, Nice et Bordeaux. Chaque prêt contracté par un de nos clients est forcément relié à l’une de ces
agences. Et vous risquez de vous poser cette question :

Admettons que je veuille calculer le chiffre d'affaires mensuel réalisé par chaque agence. Comment puis-je faire ?
Bonne question !

Il va donc falloir :
    sélectionner l’ensemble des clients de l’agence de Toulouse et calculer la somme de leurs mensualités ;
    sélectionner l’ensemble des clients de l’agence de Paris et calculer la somme de leurs mensualités ;
    etc.

Le résultat final serait ainsi une ligne par agence/ville, avec la somme des mensualités perçues par chacune d’elles.

Cette opération est ce qu’on appelle en algèbre relationnelle une agrégation. C’est une opération très courante sur des data frames, soit pour analyser les données sous un certain
angle, soit pour recalculer certaines variables, comme la moyenne des mensualités par agence.

Je vous propose de voir comment réaliser cela avec Pandas.
"""
import pandas as pd
pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)

############################
# Agregez plusieurs lignes #
############################
"""
La première méthode pour faire une agrégation avec Pandas est .group_by . 

Pour l’utiliser, vous aurez besoin de vous fixer sur une ou plusieurs colonnes, qui seront ce qu’on appelle les index de votre résultat agrégé. 

Cela vous rappelle-t-il quelque chose ? 

Eh oui ! Comme nous l’avons dit dans le chapitre précédent, l’index n’est pas forcément l’indice, ça peut être également des chaînes de caractères. Dans notre exemple, notre index 
serait la variable  ville . L’index va permettre de créer plusieurs groupes : un pour chaque valeur unique de l’index.

Après avoir choisi les colonnes sur lesquelles vous allez vous fixer, vous aurez à choisir une fonction d’agrégation. La fonction d’agrégation va prendre en entrée un groupe de 
plusieurs lignes, pour effectuer un calcul sur celles-ci dans l’optique de retourner une unique valeur pour chacun des groupes. Ici, la fonction d’agrégation serait une somme.

Si vous avez déjà fait un peu de SQL, vous aurez très certainement fait le lien entre cette opération et l’opération de GROUP BY réalisable en SQL. Les deux fonctionnent en effet 
de façon très similaire !

Considérons le data frame test suivant :
print(df)
    fix col
0   a   3
1   b   4
2   b   10
3   a   7
4   b   6

On souhaite calculer la moyenne de la variablecol pour chaque valeur de la variablefix . La ligne en Python pour faire cela est :
"""
data = [['a', 3],
        ['b', 4],
        ['b', 10],
        ['a', 7],
        ['b', 6]]

prets=pd.DataFrame(data=data, columns=['fix', 'col'])
print("\n")
print(f"data frame: \n{prets}")
print("\n")
print(f"grouper par categorie de la colonne fix: \n{prets.groupby('fix').mean()}")

"""
Décomposons ce qu’il se passe lors de l’exécution de cette ligne. Dans un premier temps, notre index sera la variablefix ; il va donc y avoir 2 groupes créés, un pour chaque 
valeur dans notre variablefix.
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857733-agregez-des-donnees-avec-pandas#/id/r-7867426

Sur chacun de ces groupes, on va appliquer la fonction d’agrégation choisie (ici, la moyenne) afin d’avoir le résultat souhaité :
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857733-agregez-des-donnees-avec-pandas#/id/r-8271370

À présent, comment calculer l’information recherchée initialement, soit le chiffre d'affaires total de chacune de nos agences ?
"""
prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv')
print("\n")
print(prets.groupby('ville').sum())

"""
Maintenant, imaginons que nous ne souhaitions la même information que par agence ET par type de prêt. Vous vous en doutez très probablement, il suffira de transmettre la liste des 
variables à placer en index :
"""
print("\n")
print(prets.groupby(['ville', 'type']).sum())

"""
Et si vous ne souhaitez avoir que le résultat sur la variable remboursement :
"""
prets.groupby(['ville', 'type'])['remboursement'].sum()

"""
On peut même appliquer des fonctions d’agrégation différentes en fonction de la colonne, voire appliquer plusieurs fonctions d’agrégation sur une même colonne. Ici, je calcule la 
moyenne et la somme deremboursement par agence, ainsi que le maximum derevenu  :
"""
prets.groupby('ville').agg({'remboursement': ['sum', 'mean'], 'revenu': 'max'})
"""
Lorsqu’on utilisegroup_by , les variables fixées en index se retrouvent… en index. C’est-à-dire que si vous essayez d’accéder à la variableville du résultat du group by, vous 
aurez simplement une erreur ! Vous serez obligé d’effectuer unreset_index pour la replacer en “colonne”.

Reprenons la dernière ligne de code présentée. Imaginons à présent que nous souhaitions avoir ce même résultat, mais sous forme d’un tableau à double entrée. Je vous propose de 
voir ça en détail dans la prochaine section.
"""

######################################
# Agregez des lignes et des colonnes #
######################################
"""
Nous souhaitons donc avoir la même agrégation, mais avec cette fois-ci, en lignes nos agences, et en colonnes les différents types de prêts.

La méthode qui vous permettra de faire cela est la méthode .pivot_table . Celle-ci prend 4 arguments en paramètres :

    index : variable(s) placée(s) en ligne ;

    columns : variable(s) placée en colonne(s) ;

    values : variable sur laquelle on va appliquer la fonction d’agrégation ;

    aggfunc : fonction d’agrégation.

La méthode permettant la transformation inverse s’appelle melt . Je vous propose de découvrir ces deux nouvelles méthodes en vidéo :
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857733-agregez-des-donnees-avec-pandas#/id/video_Player_1
"""
print("\n")
print(prets.pivot_table(index='ville', columns='type', values='remboursement', aggfunc='sum'))

#############
# Exercice #
############
"""
Contexte
Vous l’avez probablement remarqué, certains clients ont contracté plusieurs prêts au sein de notre établissement. Cela fausse donc potentiellement les calculs réalisés jusque-là. Le responsable revient vers vous avec des demandes plus précises.

Consignes
Voici l’e-mail qu’il vous a envoyé :
    Hello,
    J’aurais plusieurs demandes que je souhaiterais que tu traites dès que tu peux. On en aurait besoin pour le comité de direction prévu en fin de semaine. Pourrais-tu :
        + créer un data frame de profil client pour avoir par client toutes les informations qui le concernent, résumées en une ligne ;
        + calculer le nombre exact de personnes en état de situation bancaire risquée, à partir du taux d’endettement et de ces profils clients ;
        + calculer le bénéfice total dégagé par chacune de nos agences, par type de prêt ;
        + calculer les bénéfices moyens réalisés par chaque agence, pour chaque type de prêt, sous forme de tableau à double entrée ;
        + me communiquer la ville qui semble la plus intéressante pour y développer les prêts immobiliers ?

    Merci d’avance.
"""
import numpy as np
import pandas as pd

print("\n")
print("Exercice")
print("\n")

# traitement réalisés précédemment
prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv')

print("\n")
# calcul du taux d'endettement
prets['taux_endettement'] = round(prets['remboursement'] * 100 / prets['revenu'], 2)

# renommer taux en taux_interet
prets.rename(columns={'taux':'taux_interet'}, inplace=True)

# calculer le cout total du pret
prets['cout_total'] = prets['remboursement'] * prets['duree']

# calculer les bénéfices mensuels réalisés
prets['benefices'] = round((prets['cout_total'] * prets['taux_interet']/100)/(24), 2)

# création d'une variable risque
prets['risque'] = 'Non'
prets.loc[prets['taux_endettement'] > 35, 'risque'] = 'Oui'

"""
Pourriez vous créez un dataframe profil client pour pallier ce problème ?

Par profil client, nous entendons un dataframe où il y n'y a qu'une seule ligne par client, avec le résumé de ses informations (somme remboursement, du taux d'endettement, 
du cout_total et des bénéfices réalisés)
"""
print("\n")
profil_clients = prets.groupby('identifiant')[['remboursement', 'taux_endettement', 'cout_total', 'benefices']].sum()
profil_clients.reset_index(inplace=True)
print(profil_clients)

"""
Recalculez le nombre exact de personnes en situation bancaire risquée à partir du taux d'endettemment :
"""
print("\n")
print(f"Nombre de clients en situation bancaire risquée: \n{profil_clients.loc[profil_clients['taux_endettement'] > 35].shape[0]}")

"""
Calculez le bénéfice dégagé par chacune de nos agences, par types de prêts. Vous présenterez vos résultats sous la forme d'un tableau simple (via un group_by) :
"""
print(f"Calculez le bénéfice dégagé par chacune de nos agences, par types de prêts: {prets.groupby(['ville', 'type'])['benefices'].sum()}")

"""
Pour aller plus loin, on souhaite avoir un tableau à double entrée (via un pivot_table) présentant cette fois ci les bénéfices moyen réalisés par chaque agence, 
pour chaque type de prêt :
"""
print(prets.pivot_table(index='ville', columns='type', values='benefices', aggfunc='mean'))

#############
# En resume #
#############
"""
+ Pour agréger des données, il faut définir une ou plusieurs variables placées en index, pour former des groupes sur lesquels s’appliquera une fonction d’agrégation.
+ Le résultat final d’une agrégation contiendra autant de lignes que de valeurs différentes dans la variable ou les variables choisies en index.
+ Il existe deux méthodes en Python permettant de réaliser une agrégation :
        + la méthodegroup_by ;
        + la méthodepivot_table .
"""