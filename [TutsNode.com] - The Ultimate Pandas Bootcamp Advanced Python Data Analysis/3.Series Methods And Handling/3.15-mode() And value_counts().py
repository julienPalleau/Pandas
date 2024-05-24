# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')
# mode: The mode is the item that shows up the most frequently.
# The result below shows us that the single most occuring one serving across all countries in our alcohol dataset is 1.0
print(f"the mode: {alcohool.mode()}")

# median: The median is the middle most observation. In other words, the point in our distribution that separates the dataset into two
# equal size parts.

# means: The mean is simply the average value which we calculate as the some of all observations divided by the count of observations.

# Say we are interested in how many times this value of 1 occurs? How frequently does it show up?
print(alcohool == 1)
print(alcohool[alcohool == 1].size)
print(alcohool[alcohool == 1].sum())
# There is another hande method which will calculate the number of occurences for each value or in one go.
# value counts
print()
print(alcohool.value_counts())

'''
        value_counts()
a sorted series containing unique values and their counts

default parameters are:
                        ser.value_counts(sort=True,
                                         ascending=False,
                                         dropna=True,
                                         normalize=False)
'''
# Let's try value_count() again but with normalize parameter
print(alcohool.value_counts(normalize=True))