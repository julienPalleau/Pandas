# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

'''
        Bools As Ints
+ True  -> 1
+ False -> 0
The bool type inherits from (is a subclass of) int
bool -> int -> object
'''
print(True + 19)
print(True + True - False + True)

print(type(True))
print(type(False))

print(bool.__mro__) # mro stands for method resolution order

