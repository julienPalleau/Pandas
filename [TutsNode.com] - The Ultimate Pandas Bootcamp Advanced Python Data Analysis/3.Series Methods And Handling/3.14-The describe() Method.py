# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

print(alcohool.describe())

# you could customize a bit described for instance:
print(alcohool.describe(percentiles=[.79, .19]))

# you can filter on a type
print(alcohool.describe(percentiles=[.79, .19], include=float, exclude=object))