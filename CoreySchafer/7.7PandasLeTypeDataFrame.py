# 7.7 Pandas: le type DataFrame
# https://www.youtube.com/watch?v=P3JPvTVP4aA&list=PL2CXLryTKuwwy0jaLB10vXU6_Tkk4yPC4&index=7

"""
Tout ce que nous avons vu sur les series que ce soit loc, iloc, le slicing ou l'alignement des labels reste valable
avec le DataFrame
"""

import numpy as np
import pandas as pd

prenoms = ['liz', 'bob', 'bill', 'eve']
age = pd.Series([25, 30, 35, 40], index=prenoms)

taille = pd.Series([160, 175, 170, 180], index=prenoms)

sexe = pd.Series(list('fhhf'), index=prenoms)

df = pd.DataFrame({'age':age,
                   'taille': taille,
                   'sexe': sexe})

print(df)

# Je peux acceder à l'index des lignes:
print(f"Je peux acceder à l'index des lignes: {df.index}")

print("\n")
# Je peux acceder à l'index des colonnes:
print(f"Je peux acceder à l'index des colonnes: {df.columns}")

print("\n")
# Je peux acceder au tableau numpy sous-jacent
print(f"Je peux acceder au tableau numpy sous-jacent:\n{df.values}")

print("\n")
# Je peux regarder les 2 dernieres lignes de ma serie
print(f"Je peux regarder les 2 dernieres lignes de ma serie:\n{df.tail(2)}")

print("\n")
# Je peux faire une exploration tres rapides des proprietes statistiques de ma DataFrame:
print(f"Je peux faire une exploration tres rapides des proprietes statistiques de ma DataFrame:\n {df.describe()}")

print("\n")
# Comment acceder à 1 ligne de donnees de ma DataFrame
print(f"Comment acceder à 1 ligne de donnees de ma DataFrame:\n{df.loc['liz']}")

print("\n")
# Comment acceder à 1 ligne et 1 colonne de ma DataFrame
print(f"Comment acceder à 1 ligne et 1 colonne de ma DataFrame:\n{df.loc['liz', 'age']}")

print("\n")
# comment acceder à toute les taille de ma DataFrame
# Si je n'ai qu'un seul element passe à loc ça correspond à des lignes,
# Si je passe deux elements separes par une virgule, le premier correspond aux lignes, le deuxieme correspond aux
# colonnes.
print(f"comment acceder à toute les taille de ma DataFrame:\n{df.loc[:, 'taille']}")

print("\n")
# Sur un dataframe je peux egalement faire de l'indexation avancee comme ce qu'on a vu pour les Series.
# Exemple:
print(f"Tous les elements de mon DataFrame pour laquelle la colonne age < 32:\n {df.loc[df.loc[:,'age'] < 32]}")

print("\n")
# Une operation tres courante sur les DataFrame c'est d'enlever l'index, donc de transformer l'index en colonne
# Revoyons mon dataframe df
print(df)
print("\n")
# Si je souhaite avoir les prenoms dans une colonne et non comme un index?
df = df.reset_index()
print(df)
df=df.rename(columns={'index':'prenom'})
print(df)

print("\n")
# Si je souhaite mettre une autre colonne en index par exemple la colonne des ages:
df = df.set_index('age')
print(df)

print("\n")
# REVOYONS LA METHODOLOGIE en utilisant des methodes chainees
df = pd.DataFrame({'age': age,
                   'taille': taille,
                   'sexe': sexe})
print(df)
df = (df.reset_index()
      .rename(columns={'index': 'nom'})
      .set_index('age'))
print(df)

print("\n")
# Voyons un exemple d'alignement d'index
df1 = pd.DataFrame(np.ones((2, 2)),
                   index=list('ab'),
                   columns=list('xy'))

print(df1)

df2 = pd.DataFrame(np.ones((2, 2)),
                   index=list('ac'),
                   columns=list('xz'))
print(df2)
print("\n")
print(f'faisons la somme de df1 et df2:\n{df1+df2}')

print("\n")
# Comme nous l'avons vu avec les series je peux faire
df = df1.add(df2, fill_value=0)
print(f"fill_value ne fonctionne que si il manque une valeur à guauche ET à droite:\n {df}")

print("\n")
# Methode1 - Comment faire pour ne plus avoir de NaN?
print(f"Methode1 - Comment faire pour ne plus avoir de NaN? on utilise df.fillna(-1):\n{df.fillna(-1)}")

print("\n")
# Methode2 - Comment faire pour ne plus avoir de NaN?
print(f"Methode2 - Comment faire pour ne plus avoir de NaN? on utilise df.dropna:\n{df.dropna()}")