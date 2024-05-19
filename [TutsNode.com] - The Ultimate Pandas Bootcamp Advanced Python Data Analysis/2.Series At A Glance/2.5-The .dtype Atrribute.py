# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas as pd

ages = [27, 49, 37]
print(pd.Series(ages))

print(pd.Series(ages, dtype='float'))

# As soon as there is a string in a Series the dtype becomes object
students = ['Andrew', 'Brie', 'Kanika']
name_series = pd.Series(students)
print(name_series)
print(name_series.dtype)