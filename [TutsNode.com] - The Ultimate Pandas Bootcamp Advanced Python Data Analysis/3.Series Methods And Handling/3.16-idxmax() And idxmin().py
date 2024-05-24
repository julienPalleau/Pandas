# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

# Let's say we want to figure out the name of the country that had the most wine serving hint in 2010
print(alcohool.max())

# So now we want to figure out which country this is? What is the country label that corresponds to this maximum value?
# Again one way to get our answer is to use squre brackets and boolean mask
print()

# so technically speaking this do not return just the country, it returns the name of the serie the dtype the amount wine and the country
print(alcohool[alcohool == alcohool.max()])
# so if we want the name of the country, only then we need to get back the index
print(alcohool[alcohool == alcohool.max()].index)
# To extract the country's name, only we extract the first item
print(alcohool[alcohool == alcohool.max()].index[0])
# everythind we did here (in the 6 lines including comment above) could have been in 1 line:
print()
print(alcohool.idxmax())
print(alcohool.idxmin())
# So it is important to be careful with idxmax() and idxmin() for instance let's look at that min by another way:
print()
print('Consomation minimum')
print(alcohool.value_counts().head(1))
print(alcohool[alcohool == alcohool.min()])
# so we can see above that there are 25 countries using 1l of alcohool and idxmin() only return the first country using 1l (Brunei)
print()
print('Consomation maximum')
print(alcohool[alcohool == alcohool.max()])
print(alcohool[alcohool.idxmax()])
print(alcohool.max())

'''
            Index by min/max
+ idxmin(): returns the label of the row with minimum value
+ idxmax(): returns the label of the row with maximum value

Note: if multiple min/max values, only the first label is returned
'''