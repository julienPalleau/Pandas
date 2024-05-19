# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd

books_list = ['Fooled by Randomness', 'Sapiens', 'Lenin on the Train']
list_s = pandas.Series(books_list)
print(list_s)

# Creation of our own index
# 1st syntax
print(pd.Series(data=books_list, index=['funny', 'serious and amusing', 'kinda interesting']))

# 2nd syntax wich if fine for python and simpler
print(pd.Series(books_list, ['funny', 'serious and amusing', 'kinda interesting']))

# 3rd syntax (we know that dtype will be ojbect because the presence of a single string will force the dtype to be object)
print(pd.Series(books_list, ['funny', 'serious and amusing', 'kinda interesting'], dtype='object'))
# or
print(pd.Series(books_list, ['funny', 'serious and amusing', 'kinda interesting'], dtype='string'))
print("")
print(list_s.index)
print(type(list_s.index))

# Let's build our own rangeindex
print(list(pd.RangeIndex(start=4, stop=7, step=1)))
print(list(pd.RangeIndex(start=10, stop=-11, step=-1)))



