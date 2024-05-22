# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

# Exercice 1:
# Create a series of length 100 containing the squares of integers from 0 to 99.
# Assign it to the variable squares.

# Solution 1.1
print()
squares=[]
for i in range(0, 100):
    squares.append(i**2)

squares_11 = pd.Series(squares)
print(squares_11)

# Solution 1.2
squares_12 = pd.Series(i**2 for i in range(0, 100))
print(squares_12)

# Exercice 2:
# Extract the last three items from the square series using saqre bracket indexing.
print()
print(squares_12[-3:])
print(squares_12.iloc[-3:])

# Exercice 3:
# Repeat Step 2 but using the tail() method instead.
print()
print(squares_12.tail(3))

# Exercice 4:
# Verify that the output of steps 2 and 3 is the same using the .equals() method.
print()
print(squares_12[-3:].equals(squares_12.tail(3)))
