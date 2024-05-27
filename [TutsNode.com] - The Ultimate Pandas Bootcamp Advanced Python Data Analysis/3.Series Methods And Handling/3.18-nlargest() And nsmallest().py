# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

# min() an₫ max() are a bit limite as they provide a single value
print(alcohool.min())
print(alcohool.max())

# nlargest and nsmallses

# One solution but it is long
print(alcohool.sort_values(ascending=False)[:10])
print()
# Another shorter solution
print(alcohool.nlargest(10))
print(alcohool.nsmallest(29))