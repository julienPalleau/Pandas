# http://python-simple.com/python-pandas/creation-dataframes.php

import numpy
import pandas

"""
Création d'un dataframe :
    + un dataframe se comporte comme un dictionnaire dont les clefs sont les noms des colonnes et les valeurs sont des séries.
    + on peut le créer à partir d'une array numpy (mais ce n'est pas très pratique et le type des données est le même pour toutes les colonnes, ici float64) :
"""
ar = numpy.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5, 15]])
print(ar)
df = pandas.DataFrame(ar, index = ['a1', 'a2', 'a3'], columns = ['A', 'B', 'C', 'D'])
print("\n")
print(df)
"""
attention : si on modifie l'array numpy, cela modifie aussi le dataframe.
    + on peut aussi créer le dataframe avec un dictionnaire : 
"""
df = pandas.DataFrame({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]},
                      index = ['a1', 'a2', 'a3'])
print("\n")
print(df)

"""
    + Pour définir un dataframe avec les colonnes dans l'ordre que l'on veut :
"""
df = pandas.DataFrame({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]}, columns = ['A', 'B', 'C', 'D'])
print("\n")
print(df)

"""
    + on peut aussi donner une liste de dictionnaires : 
    donne la meme chose que ci-dessus
"""
df = pandas.DataFrame([{'A': 1.1, 'B': 2, 'C': 3.3, 'D': 4},
    {'A': 2.7, 'B': 10, 'C': 5.4, 'D': 7},
    {'A': 5.3, 'B': 9, 'C': 1.5, 'D': 15}])
print("\n")
print(df)

"""
    + on peut aussi donner un dictionnaire dont les clefs seront les index plutôt que les colonnes :
"""
print("\n")
pandas.DataFrame.from_dict({'A': [1.1, 2.7, 5.3], 'B': [2, 10, 9], 'C': [3.3, 5.4, 1.5], 'D': [4, 7, 15]}, orient = 'index')

"""
    + un index ou les colonnes d'un dataframe peuvent avoir un nom :
        - df.index.name = 'myIndexName' (si on imprime le frame dans un fichier csv avec l'index, la colonne sera nommée avec le nom de l'index).
        - df.columns.name = 'myColumnName'

    +   - df = pandas.DataFrame(columns = ['A', 'B']) : dataframe avec 0 lignes
        - df = pandas.DataFrame(columns = ['A', 'B'], index = ['a', 'b']) : dataframe avec 2 lignes et que des NA
        - df = pandas.DataFrame(0, index = [0, 1], columns = ['a', 'b']) : dataframe initialisé avec que des 0.
        - df.fillna(0, inplace = True) : le remplit avec des 0 plutot que des NaN
        - mais, attention ! : initialement, les types des colonnes sont "object" et une colonne peut avoir des valeurs de types héterogènes !
        - pour éviter ça, on peut donner un type à la création : df = pandas.DataFrame(columns = ['A', 'B'], index = ['a', 'b'], dtype = float) (ou numpy.float64, ça revient au même)

    + on peut réindexer un dataframe pour changer l'ordre des lignes et/ou des colonnes, ou n'en récupérer que certaines : df.reindex(columns = ['C', 'B', 'A'], index = ['a2', 'a3'])
    + df.dtypes : les types des différentes colonnes du dataframe, ici : 
        A    float64
        B      int64
        C    float64
        D      int64
        
    + si les séries ont des index, le dataframe utilise ces index pour construire le dataframe : df = pandas.DataFrame({'col1': pandas.Series([2, 3, 4], index = ['a', 'b', 'c']), 
      'col2': pandas.Series([6, 7, 8], index = ['b', 'a', 'd'])}) donne : 
         col1  col2
        a     2     7
        b     3     6
        c     4   NaN
        d   NaN     8
        
    + On peut mettre une seule valeur pour une colonne dans la définition d'un dataframe : df = pandas.DataFrame({'a': 1, 'b': [2, 3, 4], 'c': [5, 6, 7]})
    + df.info() : imprime des infos sur le dataframe : les noms et types des colonnes, le nombre de valeurs non nulles et la place occupée.
    + df.head(2) : renvoie un dataframe avec les 2 premières lignes. Idem avec df.tail(2) pour les deux dernières.
    + df.head(), df.tail() : les 5 premières ou les 5 dernières.
    + df.columns : les noms des colonnes, par exemple Index(['A', 'B', 'C', 'D'], dtype='object').
    + df.columns.values : le nom des colonnes sous forme d'array numpy.
    + df.index : les noms des lignes (individus), par exemple Index(['a1', 'a2', 'a3'], dtype='object').
    + df.index.values : le nom des lignes sous forme d'array numpy.
    + df.values : pour récupérer le dataframe sous forme d'array numpy 2d.
    + df.describe() : renvoie un dataframe donnant des statistiques sur les valeurs (nombres de valeurs, moyenne, écart-type, ...), mais uniquement sur les colonnes numériques 
      (faire df.describe(include = 'all') pour avoir toutes les colonnes) : 
                            A          B         C          D
        count  3.000000   3.000000  3.000000   3.000000
        mean   3.033333   7.000000  3.400000   8.666667
        std    2.119748   4.358899  1.951922   5.686241
        min    1.100000   2.000000  1.500000   4.000000
        25%    1.900000   5.500000  2.400000   5.500000
        50%    2.700000   9.000000  3.300000   7.000000
        75%    4.000000   9.500000  4.350000  11.000000
        max    5.300000  10.000000  5.400000  15.000000
    + df.describe(include = 'all').to_csv(sys.stdout, sep = '\t') : permet d'imprimer les stats sur toutes les colonnes (numériques ou non).
    + on peut régler la largeur d'impression quand on imprime un dataframe avec : pandas.set_option('display.width', 120)    
"""

"""
Dimension d'un dataframe:

    + df.shape : renvoie la dimension du dataframe sous forme (nombre de lignes, nombre de colonnes)
    + on peut aussi faire len(df) pour avoir le nombre de lignes (ou également len(df.index)).
    + on peut aussi faire len(df.columns) pour avoir le nombre de colonnes.
    + df.memory_usage() : donne une série avec la place occupeée par chaque colonne (sum(df.memory_usage()) donne la mémoire totale occupée).
"""

"""
Un dataframe peut avoir un nom pour son index de ligne et son index de colonnes:
    + df.index.name = 'myRow'; df.columns.name = 'myCol'
    + ce nom sera utilisé comme nom de colonne si on fait df.stack().reset_index()
"""

"""
On peut réaligner 2 dataframes entre eux
    + df1.align(df2) : renvoie un tuple de 2 dataframes réalignés, avec par défaut, une jointure externe sur les colonnes et les lignes (index) : ils contiennent la réunion des colonnes et la réunion des lignes, dans le même ordre.
    + df1.align(df2, join = 'inner') : les colonnes et les index communs.
    + il y a aussi la possibilité de faire des jointures externes gauche ou droite avec join = 'left' ou join = 'right'
    + on peut faire l'alignement que sur les lignes avec df1.align(df2, axis = 0) (idem pour les colonnes avec axis = 1).
"""

"""
un dataframe peut avoir 0 colonne
    + par exemple df0 = pandas.DataFrame({}, index = ['a', 'b', 'c'])
"""

"""
Quand on a un dataframe avec une seule colonne ou une seule ligne, on peut le transformer en series par : df.squeeze() (ne fait rien sur une series ou sur un dataframe avec 
plusieurs colonnes)
"""