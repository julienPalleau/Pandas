# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling

import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

print(alcohool.head())
print()

# What we are doing below is in the serie above elementn+1 - elementn
print(alcohool.diff().head())

# Here we are taking a difference with the previous, previous country or elementn+2 - elementn
print()
print(alcohool.diff(periods=2).head())

'''
        diff()
    the first discrete element-wise difference in a series
    a   v1
    b   v2              ser.diff(periods=1)
    c   v3
    dtype: object
    
                        periods=1       periods=-1       periods=2
                        v2 - v1         v1 - v2          v3 - v1
                        v3 - v2         v2 - v3          v4 - v2
    
'''