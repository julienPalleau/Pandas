# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase

letters = list(ascii_lowercase)
alphabet = pd.Series(letters)
print(alphabet.head(6))

# 1. What is the first letter
print("1. What is the first letter")
print(alphabet[0])
print()

# 2. What is the 11th letter?
print("2. What is the 11th letter?")
print(alphabet[10])
print()

# 3. What are the first three letters?
print("3. What are the first three letters?")
print(alphabet[:3])
print()

# 4. What are the sixth through tenth letters?
print("4. What are the sixth through tenth letters?")
print(alphabet[5:10])
print()

# 5. What are the last six letters?
print("5. What are the last six letters?")
print(alphabet[-6:])
print()
