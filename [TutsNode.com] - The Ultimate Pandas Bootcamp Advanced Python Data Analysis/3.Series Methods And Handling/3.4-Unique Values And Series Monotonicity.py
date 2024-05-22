# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohol = alcohol.squeeze('columns')

# Check if the serie contains a sequence of unique values:
print(alcohol.is_unique)
print(alcohol.head().is_unique)

# There is another attribut nunique that gives us the number of unique items:
# if you wish to exclude the Na you can use dropna=False
print(alcohol.nunique(dropna=False))

# Another interesting attribute is_monotonic attribut which tells you if the series change
print(pd.Series([1,2,3]).is_monotonic_increasing)
print(pd.Series([1,2,3,2,1]).is_monotonic_increasing)
print(pd.Series([1,2,3,3,3]).is_monotonic_increasing)
print(pd.Series(reversed([1,2,3])).is_monotonic_increasing)
print(pd.Series(reversed([1,2,3])).is_monotonic_decreasing)
#