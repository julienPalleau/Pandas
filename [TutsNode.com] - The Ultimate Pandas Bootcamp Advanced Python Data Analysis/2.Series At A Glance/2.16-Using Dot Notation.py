# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

labeled_alphabet = pd.Series(data=list(ascii_lowercase), index=map(lambda x: 'label_' + x, list(ascii_uppercase)))
print(labeled_alphabet['label_V'])

# we could also use dot notation
# remember
print(labeled_alphabet.dtype)
print(labeled_alphabet.size)
print(labeled_alphabet.name)

# Similarly, we can access the value associated with the label in using dot following by the label,
# and the two lines below are completely functionnaly equivalent,
# but this convenience in syntax comes with a couple of limitations, so dot not notation is not as flexible as square brackets
#
print(labeled_alphabet['label_V'])
print(labeled_alphabet.label_V)

# Let's see a couple of examples:
# Let's say we want to slice label_alphabet
print(labeled_alphabet['label_V':'label_X'])
# we can't do anything similar using dot access
