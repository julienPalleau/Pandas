# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857549-filtrez-les-donnees-du-data-frame

import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)

print("""
#####################################
# Filtrez les donnees du data frame #
#####################################
Imaginons les situations suivantes :

    pour une offre commerciale spécifique, on cherche à ne sélectionner que les hommes de notre data frame ;

    on souhaite identifier les hauts revenus parmi notre clientèle. Pour cela, on souhaite sélectionner tout ceux gagnant mensuellement plus de x € ;

    on souhaite identifier les clients dits “risqués”, c’est-à-dire ceux qui ont un taux d’endettement supérieur aux 35 % légaux.

Jusqu’à présent, nous avons été capables de sélectionner des colonnes spécifiques et de les manipuler à notre guise. Mais les exemples précédents ne peuvent être satisfaits avec 
de simples manipulations de colonnes : il faut appliquer une condition spécifique pour ne sélectionner que les lignes pertinentes.

Cette opération est ce qu’on appelle une restriction, ou un filtrage. Naturellement, Pandas permet de faire cela, pour avoir un contrôle total sur nos données. Voyons cela 
ensemble !
Appliquez la sélection via des indices

Le premier type de sélection est réalisé via des indices. Il se fait via la méthode.iloc . 

Pour rappel, un indice est la position à laquelle se trouve un élément au sein d’un tableau, que ce soit une liste, une Series ou un array. En Python, les indices commencent à 
0 : ainsi, le premier élément aura pour indice 0, le second 1, etc.

La méthode.iloc suit la syntaxe suivante :  mon_dataframe.iloc[indice_ligne, indice_colonne] .

Prenons un exemple concret : on souhaite sélectionner le nom du premier client de notre base de données. Comme c’est le premier client, son indice de ligne sera 0. Nous souhaitons 
sélectionner son nom ; la variable nom est la 3e variable de notre data frame, l’indice de sa colonne sera donc… 2. Eh oui ! Pour les colonnes aussi, les indices commencent à 0. 
Le code de sélection serait donc : 
Exemple de sélection via un indice - la sélection permet de récupérer le nom du premier client 'Laurent Dagenais'
Exemple de sélection via un indice

Cela correspond bien au nom de notre premier client.

Maintenant, admettons que je souhaite sélectionner le nom des 10 premiers clients, comment procéder ?

Comme avec les arrays, nous pouvons utiliser l’opérateur :  pour sélectionner la plage souhaitée ! Voici quelques exemples :
""")

##########################################
# Appliquez la sélection via des indices #
##########################################
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857549-filtrez-les-donnees-du-data-frame#/id/r-7857486
# Chargement du fichier
clients = pd.read_csv("clients.csv")

# sélectionner le nom des 10 premiers clients :
print(clients.iloc[:10, 2])

############################################
# Utilisez la sélection via des conditions #
############################################
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857549-filtrez-les-donnees-du-data-frame#/id/r-7857537
"""
Pour être tout à fait honnête avec vous, les data frames possèdent de nombreuses méthodes, comme vous avez pu commencer à vous en rendre compte. Mais de toutes, il y en a 
certainement une que vous allez utiliser et réutiliser à outrance : c’est la méthode.loc!

Celle-ci suit la syntaxe suivante :

mon_dataframe.loc[ condition sur les lignes, colonne(s) ]  .

C’est à première vue très simple, mais nous allons voir que cette syntaxe peut en pratique devenir vite complexe, et peut permettre en même temps une grande flexibilité. C’est LA 
méthode qui pourra répondre à près de 90 % de vos besoins en termes de sélection d’une partie de vos données. La source de ce chiffre ? OK, c’est un avis totalement personnel ! 
Mais laissez-moi vous montrer pourquoi je suis aussi sûr de moi.

Une autre option de la méthode .loc est la sélection par index. Avant d’aller plus loin sur cet aspect, laissez-moi redéfinir la différence entre des index et des indices ! 
Les indices, comme nous l’avons vu plus haut, sont la position intrinsèque d’un élément au sein d’un tableau. Les index, en revanche, correspondent à une valeur qui est associée à 
chaque ligne. C’est ce que vous voyez sur la gauche de votre data frame :

Par défaut, ils correspondent… aux indices ! Mais ils peuvent ne pas être numériques ; on pourrait par exemple fixer le nom de la personne comme index, si on est sûr qu'il n'y 
aura pas de doublons.

Faisons un simple tri pour bien comprendre la différence entre l’indice et l’index :
Différence entre index et indice - l'indice correspond à la numérotation de chaque ligne à partir de 0 et l'index correspond à la colonne identifiant
Différence entre index et indice

Cette situation est intéressante, car si on regarde notre première ligne, son index est 13. Pourtant, c’est bel et bien la première ligne, donc son indice est 0 !!!

Je pense que vous commencez à comprendre la différence : un indice est relatif aux opérations réalisées. Un individu peut avoir le premier indice à un moment, et un tout autre 
indice en fonction du tri effectué. En revanche, l’index est intrinsèque aux lignes au sein d’un data frame. Peu importe les opérations effectuées, que ce soit un tri, une 
suppression, etc., l’index sera toujours le même ! La seule condition, c’est que chaque ligne doit avoir un index unique : c’est-à-dire qu’il ne doit pas y avoir deux fois la même 
valeur au sein d’un index ; on ne pourra par exemple pas avoir 2 fois l’index 0, etc.

Pourquoi je vous parle de tout cela ?

Parce qu’il est possible de faire une sélection au sein d’un data frame selon les index, avec la méthode.loc.

Faites le test avec les lignes suivantes :
"""
print(clients.loc[0:10, :])
print(clients.iloc[0:10, :])

"""
Il est d’ailleurs possible d’accéder à la liste des index d’un data frame via l’attribut.index . Par exemple,clients.indexnous renverra l’ensemble des index de notre data frame.

Il est parfois intéressant, après avoir effectué certaines opérations, de réinitialiser ces index – nous verrons un exemple concret, dans la prochaine section, où cela est même 
nécessaire. C’est possible via la méthode.reset_index() :
"""
# Creation d'un data frame trie pour desordonner les Index
print("\n")
df_temp = clients.sort_values('nom')
print(f"Creation d'un data frame trie pour desordonner les Index: \n{df_temp}")