# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling

'''
Exercice 1
Read the drinks.csv dataset again, this time bringing in the beer_servings sequence into a new series with country again acting as the index.
Assign this series to the variable beers.
link to data: https://andybek.com/pandas-drinks
'''
import pandas as pd
import numpy as np

# Check the column names only in order to find if beer_servings is part of the columns and check its syntax
# print(alcohool.columns)
alcohool = pd.read_csv('drinks.csv', usecols=['country', 'beer_servings'], index_col='country').squeeze('columns')

print(type(alcohool))

# dropna() functions to ...
print(alcohool.dropna())
#
# '''
# Exercice 2
# Calculage the mean, median, and standard deviation of beer servings in beers. Is the distribution right or left skewed?
# '''

print(f"alcohool mean: {alcohool.mean()}")
print(f"alcohool median: {alcohool.median()}")
print(f"alcohool median can also be computed with quantile 0.5: {alcohool.quantile(.5)}")
print(f"alcohool standard deviation: {alcohool.std()}")
print(f"The standard deviation is also the square root of variance: {alcohool.var()**(1/2)}")
print(f"The standard deviation is also the square root of variance: {np.sqrt(alcohool.var())}")
# To answer the second part of the question about the skew: the meen is much bigger that the median, so we can conclude this is a right skew
print(alcohool.describe())

#
# '''
# Exercice 3
# Since the first 10 countries from beers. Are these relatively large or small relative to the rest of the sample?
# BONNUS: to answer : that, we could compare each value to the mean or medium. An even better approach would be to calculate standard scores,
# or z-scores as they are known.
# '''
print()
from scipy import stats

print(alcohool[:10])
print(alcohool.head(10))
print(alcohool[:10] - alcohool.mean())
# to make the result of the line above easier to digest, we can:
print((alcohool - alcohool.mean()).apply(lambda x: 'low' if x < 0 else 'high').value_counts())

# A most statical way to deal with this would be to use z-score
'''
                The z-score
                z = (xi - mu)/sigma ou - the z score = (the data point in question - the mean)/the standard deviation)
'''
z_score = (alcohool - alcohool.mean()) / alcohool.std()
print()
print(f"z_score: {z_score}")
print(f"z_score max: {z_score.max()}")

print(f"idxmax: {alcohool.idxmax()} -> {alcohool[alcohool.idxmax()]}")
