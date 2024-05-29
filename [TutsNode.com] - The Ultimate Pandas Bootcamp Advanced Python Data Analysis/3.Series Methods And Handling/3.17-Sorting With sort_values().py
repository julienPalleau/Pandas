# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohol = alcohol.squeeze('columns')

# For sorting our series, we have two options: we could sort by values or by the index
# We are now going to talk about sorting by values
print(alcohol.sort_values())

# How to sort in the opposite order?
print(alcohol.sort_values(ascending=False, na_position='last'))  # na_position='last' is the default one, so it can be omitted

# We could also specify the sorting algorithme: default is 'quicksort' but there are also 'mergesort' and 'heapsort,' however, the recommendation
# is to keep default one or 'quicksort' except if explicitely requested to use one of the two others. As each of them has different performance

print()
print(alcohol.head())
# The serie is still unsorted why that?
# sort_values() is one of those methods that return a copy of series it returns a new series where values are sorted without affecting the original
# set.
# If we want to sort the existing series, again, we have two options:
# 1 - reassignment
# 2 - inplace parameter
print()
A = alcohol.copy()
A.sort_values(ascending=False, na_position='last', kind='quicksort', inplace=True)
print(A)

