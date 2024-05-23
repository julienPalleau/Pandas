# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')
print(alcohool.sum())

# average
print(alcohool.count())
print()
print(f"compute mean: {alcohool.sum()/alcohool.count()}")
# or
print(f"function mean: {alcohool.mean()}")

'''
            Median
The middlemost element in a sorted list of numbers.
10, 11, 12, 13, 14, 15, 16
            |
            
10, 11, 12, 13, 14, 15, 16, 17
            ------
               |
            (13+14)/2=13.5
'''

print(f"the mediand: {alcohool.median()}")

print(f"the quantile .5: {alcohool.quantile(.5)}")

alcohool.hist()
plt.show()
print()
# IQR
iqr = alcohool.quantile(.75) - alcohool.quantile(.25)
print(iqr)
print()
# min and max
print(f"minimum of our alcohool serie: {alcohool.min()}")
print(f"maximum of our alcohool serie: {alcohool.max()}")
print()
# Standard deviation is square root of variance
print(f"Standard deviation: {alcohool.std()}")

# Variance
print(f"Variance: {alcohool.var()}")

# Obviously the expression below should return True I had to round it up with fstring as the result of variance stdv do not have the same precision.
print(f"{alcohool.std()**2:2f}" == f"{alcohool.var():2f}")
