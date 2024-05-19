# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas as pd

students = ['Andrew', 'Brie', 'Kanika']
# In the line below we are passing students (python list) as an argument to the data parameter
print(pd.Series(students))

# This is equivalent to say:
# In the line below data is the parameter (variables in a method definition where arguments are the values we are passing like above)
# arguments: are actuals (actual data we are passing)
# parameter: are variables
print(pd.Series(data=students))