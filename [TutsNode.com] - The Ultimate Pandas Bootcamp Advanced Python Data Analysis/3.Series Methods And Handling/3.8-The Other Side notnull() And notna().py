# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

'''
We've seen how to isolate nulls in more ways than one but what if we are interested in everything except nulls ?
For that we have two really straight forward methods at our disposal:
    + notnull()
    + the second method doesn't work alcohol.loc[alcohol.notnull()]
'''
alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohol = alcohol.squeeze('columns')
print(alcohol.notnull())

print()
print(alcohol.loc[alcohol.notnull()])
print()
print(alcohol.notnull().sum())
print(alcohol.count())

print()
print(alcohol.notnull().sum() + alcohol.isnull().sum() == alcohol.size)

# Like null has an alias for na, notnull has an alias for notna
print()
print(alcohol.notna().sum())
print(alcohol.loc[alcohol.notna()])
