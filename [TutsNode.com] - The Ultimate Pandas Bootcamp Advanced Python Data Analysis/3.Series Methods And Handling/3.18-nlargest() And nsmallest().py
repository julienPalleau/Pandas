# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohol = alcohol.squeeze('columns')

# min() an₫ max() are a bit limite as they provide a single value
print(alcohol.min())
print(alcohol.max())

# nlargest and nsmallses

# One solution but it is long
print(alcohol.sort_values(ascending=False)[:10])
print()
# Another shorter solution
print(alcohol.nlargest(10))
print(alcohol.nsmallest(29))