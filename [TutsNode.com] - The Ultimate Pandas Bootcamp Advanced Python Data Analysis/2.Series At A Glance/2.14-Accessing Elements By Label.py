# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

labeled_alphabet = pd.Series(data=list(ascii_lowercase), index=map(lambda x: 'label_' + x, list(ascii_uppercase)))
print(labeled_alphabet.head(3))

# 1. What is the first letter
print("1. What is the first letter")
print(labeled_alphabet.iloc[0])
print(labeled_alphabet['label_A'])
print()

# 2. What is the 11th letter?
print("2. What is the 11th letter?")
print(labeled_alphabet.iloc[10])
print(labeled_alphabet['label_K'])
print()

# 3. What are the first three letters?
print("3. What are the first three letters?")
print(labeled_alphabet.iloc[:3])
print(labeled_alphabet[:'label_C'])
print()

# 4. What are the sixth through tenth letters?
print("4. What are the sixth through tenth letters?")
print(labeled_alphabet.iloc[5:10])
print(labeled_alphabet['label_F':'label_J'])
print()

# 5. What are the last six letters?
print("5. What are the last six letters?")
print(labeled_alphabet.iloc[-6:])
print(labeled_alphabet['label_U':])