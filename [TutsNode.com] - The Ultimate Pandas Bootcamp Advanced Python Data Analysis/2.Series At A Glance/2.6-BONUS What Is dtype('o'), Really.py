# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas as pd

'''
numpy expects homogenous ("same type") data
numpy love that because it always take the same space to store a float

However for string it is less predictible as strings are variable length!
So to solve this problem of variable length, numpy store an obj_ref on each word of the string:
numpy:
-------------------------------
| Obj_ref | Obj_ref | Obj_ref |
-------------------------------
   |           |        |
   |      ---------------     
   |      |    |
   |      |     -------------   
   |      |                |
------------------------------------------
| have | been | brought | good | weather |
------------------------------------------
'''
heights = [167.4, 173.2, 190.0]
print(pd.Series(heights))

# we can see below that pd.Series(height2) has a dtype object now.
# The reason for that is the presence of the string '173.2', forces pandas to store pointer reference instead of
# the actual float numbers themselves.
heights2 = [167.4, '173.2', 190.0]
print(pd.Series(heights2))


