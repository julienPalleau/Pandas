# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

# In the previous chapter we had:
alphabet = pd.Series(list(ascii_lowercase))
# labeled_alphabet = pd.Series(data=list(ascii_lowercase), index=map(lambda x: 'label_' + x, list(ascii_uppercase)))
# print(labeled_alphabet)

# There is another easier way to proceed
print(alphabet.add_prefix('label_'))

# There is another method called suffix
print(alphabet.add_suffix('_some_cool_ending'))