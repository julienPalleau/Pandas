# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohol = alcohol.squeeze('columns')

'''
Exercice 1
Isolate the non-nulls in the alcohol series and assign them to the variable wine_servings.
'''
wine_servings = alcohol.loc[alcohol.notnull()]
print(wine_servings)

'''
Exercice 2
What is the total wine consumed by countries in wine_serving?
'''
print(alcohol.sum())
#or
# print(wine_servings.sum())

'''
Exercice 3
In the wine_servings dataset, what was the total wine consumed by countries that consumed less than 100 servings?
'''
print(wine_servings[wine_servings < 100].sum())