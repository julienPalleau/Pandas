# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')


alcohol = alcohol.squeeze('columns')

# Length of the serie
print(alcohol.size)

# we can get this information and other (Name of the serie, Length, dtype) in printing the Data serie.
print()
print(alcohol)

# We can access to values only with the line below
print()
print(alcohol.values)

# We can access to index only with the line below
print()
print(alcohol.index)

# We can acces to the length of series and index which are equals:
print()
print(alcohol.values.size == alcohol.index.size)

# Let's look at alcohol shape which will return a tuple:
# In case of Serie the tuple has only on value as there is one dimension
# In case of Data Frame, the tuple has 2 values because of 2 dimensions
print()
print(alcohol.shape)
print(alcohol.size==alcohol.shape[0])

# Let's use the built-in len function
print()
print(len(alcohol))

'''
        Size and Shape
+ .size: number of elements in the series
    series.size # 193
    
+ .shape: tuple of the dimensions
    for a series: (1D) shape, i.e. length for series
    series.hape # (193,)
    
+ len(): python built-in function
    len(series) # 193
'''
