# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling

import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

'''
            Variance
    The average of squared differences from the mean
        s^2=Somme(x-xbarre)^2
                    n-1
So the formula above means: For each observation find its difference relative to the mean and then square that difference
and find the sum of all those differences. Finally divide the sum of all of those differences by the number of observation in the sample - 1


xbarre -> mean



'''
# The variance via var() function on the first line and via the formula explained above and great we got the same result !
print(f"variance: {alcohool.var()}")
print(f"alcohool variance: {(alcohool.subtract(alcohool.mean())**2).sum()/(alcohool.count() - 1)}")

# The standard deviation is the square root of variance
print(f"standard deviation: {alcohool.std()}")
print(f"alcohool standard deviation: {((alcohool.subtract(alcohool.mean())**2).sum()/(alcohool.count() - 1))**(1/2)}")
