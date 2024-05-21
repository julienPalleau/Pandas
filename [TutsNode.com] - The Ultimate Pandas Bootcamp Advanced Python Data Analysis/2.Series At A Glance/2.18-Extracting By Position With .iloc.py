# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

# iloc => integer loc => index by position
# loc => location => indexing by label

labeled_alphabet = pd.Series(data=list(ascii_lowercase), index=map(lambda x: 'label_' + x, list(ascii_uppercase)))
print(labeled_alphabet.iloc[0])
print(labeled_alphabet.iloc[1])
print(labeled_alphabet.iloc[2])
print(labeled_alphabet.iloc[1:3])
print(labeled_alphabet.iloc[[1, 4, 9]])
