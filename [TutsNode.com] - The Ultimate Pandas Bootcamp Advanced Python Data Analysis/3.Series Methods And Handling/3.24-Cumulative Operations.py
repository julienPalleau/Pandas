# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling

import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

# sum
print(f"sum of alcohool: {alcohool.sum()}")
print(f"cumulative sum of alcohool: {alcohool.cumsum()}") # there is a default parameter skipna=True

# prond
print()
print(f"prod of alcohool: {alcohool.prod()}")
print(f"cumulative prod of {alcohool.cumprod()}")
print(f"the last element of alcohool.cumprod() == alcohool.prod(): {alcohool.cumprod().iloc[-1] == alcohool.prod()}")

# we also have cummin and cummax
print()
print(f"minimum of alcohool: alcohool.min()")
print(f"cumulative min of {alcohool.cummin()}")

print()
print(f"maximum of alcohool: alcohool.max()")
print(f"cumulative max of {alcohool.cummax()}")