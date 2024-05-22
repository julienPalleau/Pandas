# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

'''
        Sequential vs Vectorized ops
+ vectorization: running operations on entire arrays
            Sequential              
           --------- 
          |  -----  |
func()    |  |   |  |
          |  -----  |
func()    |  |   |  |
          |  -----  |
func()    |  |   |  |
          |  -----  |
          |         |
           ---------
           
           
            Vectorized
           --------- 
          |  -----  |
          |  |   |  |
          |  -----  |
func()    |  |   |  |
          |  -----  |
          |  |   |  |
          |  -----  |
          |         |
           ---------

ufunc -> universal functions
'''
ser = pd.Series(data=[True, False, None, 2], dtype=float)
print(np.isnan(ser))
print(ser)
print()

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
print(alcohol[np.isnan].size)
print(alcohol[alcohol.isna()])
