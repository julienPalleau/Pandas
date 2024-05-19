# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd

int_series = pd.Series(range(60))

# To quickly look at the size of the object: 2 solutions
# Solution 1:
print(int_series.size)

# Solution 2:
print(len(int_series))


# look at the head and tail of series
# to get an overview of firsts 5 lines
print(int_series.head())

# to get an overview of lasts 5 lines
print(int_series.tail())

# to get an overview of firsts 3 lines
print(int_series.head(3))  # or print(int_series.head(n=3))

# to get an overview of lasts 3 lines
print(int_series.tail(3))  # or print(int_series.tail(n=3))

# Pandas truncate by himself the result when there are lots of values, for example:
print()
print(pd.Series(range(100)))
# To change the behavior illustrated above:
pd.set_option('display.max_rows', None)
print(pd.Series(range(100)))



