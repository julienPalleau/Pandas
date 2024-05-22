# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

# Read the all csv file
# print(pd.read_csv('drinks.csv'))
#
# Filter 2 columns: country and wine_servings
print(pd.read_csv('drinks.csv', usecols=['country', 'wine_servings']))

# Put country as index
print()
print(pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country'))

# Let's assign the result from previous line to a variable
alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')

# we can use DataFrame.squeeze('columns') to get a Series
print()
print(alcohol.head())
print(type(alcohol))

print()
alcohol = alcohol.squeeze('columns')
print(type(alcohol))

