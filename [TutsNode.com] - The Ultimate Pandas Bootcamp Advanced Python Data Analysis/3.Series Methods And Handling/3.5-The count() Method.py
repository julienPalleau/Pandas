# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohol = alcohol.squeeze('columns')

# https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size
# https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#pandas-series-count

print(alcohol.count())
print()
# The difference 162 vs 193 is explained by Pandas doc (links above) in other words:
# The pandas.Series.count() method return number of non-NA/null observations in the Series.
# i.e:
s = pd.Series([0.0, 1.0, np.nan])
print(s.count())
# 2

print()
print(alcohol.hasnans)

# Where the pandas.Series.size() return the number of elements in the underlying data.
# Example:
print()
s = pd.Series([0.0, 1.0, np.nan])
print(s.size)
# 3

