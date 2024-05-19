#W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance

'''
Series are:
    + one-dimensional
    + labeled arrays
    + of any data type

Or, said differently...
    + a sequence of values
    + with associated labels
'''
import pandas as pd

students = ['Andrew', 'Brie', 'Kanika']
print(type(students))
print(pd.Series(students))

ages=[27, 49, 37]
print(pd.Series(ages))

heights = [167.4, 173.2, 190.0]
print(pd.Series(heights))

mixed = [True, 'say', {'my_mood':100}]
print(pd.Series(mixed))