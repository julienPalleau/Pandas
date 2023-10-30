# 7.6 Pandas: introduction aux Series et aux indexes
# https://www.youtube.com/watch?v=67Sa81g2zLI

"""
#######################################
# Difference entre serie et DataFrame #
#######################################
Les series sont des tableaux à une dimension sur lesquelles on va mettre un index
Les DataFrames sont des tableaux à deux dimensions sur lesquelles on va mettre des index (sur les lignes et sur les
colonnes)

#####################################
# Qu'est-ce qu'un index dans Pandas #
#####################################
- Un index est un objet imuable qui est a la frontiere du set et de la liste.
- Un index contient des elements qui sont hashables, comme un set, et il est sliceable, comme une liste.
- De plus, l'index va definir une relation d'ordre sur les elements qui sont stockes, et il peut contenir des
elements dupliques.
- Un index sur un Series va permettre d'offir à la series une interface qui est à la fois une interface de liste
et une interface de dictionnaire.
"""

# Example de serie et d'index
import pandas as pd

s = pd.Series([20, 30, 40, 50],
              index=['eve', 'bill', 'liz', 'bob'])

print(s)

# Accedons aux valeurs de la serie:
print("\n")
print(f'Valeur de la serie: {s.values}')

# Accedons à l'index:
print("\n")
print(f'Index de la serie: {s.index}')

# Accedons a un element de la serie
print("\n")
print(
    f"Un Element de la serie pandas: {s.loc['eve']}")  # il est important de toujours utiliser loc pour acceder aux elements.

# Accedons a plusieurs elements de la serie avec le slice
print("\n")
print(f"Plusieurs elements de la serie pandas:\n{s.loc['eve': 'liz']}")  # !!! le slice de pandas va de i a j inclus !!!

# Comme on peut faire des slices sur les labels quel est la relation d'ordre sur les labels?
# La relation d'ordre est definie à la creation de la serie par exemple:
print("\n")
s = pd.Series([20, 30, 40, 50],
              index=['eve', 'liz', 'bill', 'bob'])  # j'ai interverti bill et liz
# je recrée le meme slice que precedemment mais sur la nouvelle serie (avec bill et liz interverti)
print(f"Plusieurs elements de la nouvelle serie pandas:\n{s.loc['eve': 'liz']}")

# !!! Cependant, il y a un cas pour lequel le sicing ne marche pas: Le slicing sur les labels ne va pas etre defini,
# si on a des labels dupliqués et qu'en plus, mon index n'a pas ete trie.
# Dit autrement si je n'ai pas de label duplique le slicing fonctionnera toujours et si mon index a ete trie, le
# slicing fonctionnera toujours.
# Regardons un example:
print("\n")
annimaux = ['chien', 'chat', 'chat', 'chien', 'poisson']
proprio = ['eve', 'bob', 'eve', 'bill', 'liz']
s = pd.Series(annimaux, index=proprio)
print(f'series avec duplicats:\n{s}')
# print(s.loc['eve':'liz']) Cela donne une erreur à cause des duplicats

# Afin de fixer le probleme il suffit de trier l'index
print("\n")
s = s.sort_index()
print(f"On a pu faire un slice sure une serie avec des indexes dupliques car on a trie la serie:\n{s.loc['eve':'liz']}")
print("\n")
print(f"Si je regarde ma nouvelle serie avec l'index trie:\n{s}")

# Pour finir sur cette notion d'indexation il existe un autre attribut qui s'apelle iloc.
# Iloc me permet dacceder à des attributs non plus par leur label, mais par leur rang dans l'index.
# iloc[0] me permet d'obtenir le premier element de la serie
print("\n")
print(s.iloc[0])
print(
    f"slice sur index donc comportement habituel de i a j-1:\n{s.iloc[1:3]}")  # slice sur index donc on retrouve le comportement habituel du slice de i a j-1

# !!!!!!!!!!!!!! Slice sur Iloc et slice sur Loc !!!!!!!!!!!!!!!!!!!!!!!
# slice sur iloc ou slice sur index -> comportement classique du slice de i à j-1
# slice sur loc ou slice sur label -> slice de i à j inclus

# Comme les tableaux numpy les series acceptent egalement la notion d'indexation avance
# Exemple:
print("\n")
print(s.loc[(s == 'chien') | (s == 'poisson')])


# Je peux maintenant faire de l'affectation en disant que tous ceux qui valent chien ou poisson sont remplaces par autre
# NaN Not a Number
print("\n")
s.loc[(s == 'chien') | (s == 'poisson')] = 'autre'
print(f"nouvelle serie ou l'on a remplace chien et poisson par autre:\n{s}")


# Notion d'alignement d'index
# Creons 2 series:
print("/n")
s1 = pd.Series([1, 2, 3], index=list('abc'))
s2 = pd.Series([5, 6, 7], index=list('acd'))

print(f"serie s1:\n{s1}")
print(f"serie s2:\n{s2}")
print(f"serie s1 + s2:\n{s1 + s2}")

# On remarque que S1 et S2 sont des int64 (executer le pgm) et que S1 + S2 est un float 64 car les NaN sont definis
# dans les float 64

# Il est possible d'assigner une valeur par defaut aux NaN:
print(s1.add(s2, fill_value=50))