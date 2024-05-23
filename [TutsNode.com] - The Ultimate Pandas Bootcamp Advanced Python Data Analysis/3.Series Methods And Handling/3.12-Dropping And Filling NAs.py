# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohol = alcohol.squeeze('columns')
# alcohol.dropna() # Modify the list in place which means the original Series is not altered
# print(alcohol)
# alcohol = alcohol.dropna() # Modify the list in place so if we want the result to be stored we have to assign the result
# print(alcohol)

# another way is to use inplace parameter
print()
alcohol.dropna()
print(alcohol)  # which is the same as alcohol.dropna(inplace=False) so the original list is not modified
print()
# alcohol.dropna(inplace=True)
# print(alcohol)

# Droping na is one alternative another one could be to replace na by something more meaningfull
print(alcohol.fillna(100, inplace=False))  # inplace=False is the default and therefore is not requested except for making things clearer

'''
        Dropping Or Filling NAs
+ .dropna(): excludes NAs from the series
+ .fillna(): replaces NAs with something else

Note: both methods return a copy of the series unless ser.fillna('new value', inplace=True)
'''