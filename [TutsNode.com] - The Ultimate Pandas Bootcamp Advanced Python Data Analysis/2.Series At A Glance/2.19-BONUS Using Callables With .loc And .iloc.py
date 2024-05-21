# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

'''
    Indexing With Callables
+ used for highly customizable indexing
+ work with [], .loc and .loc
+ a single-argument function that returns indexing output
                                                    |
                                                + a list of labels
                                                + list of booleans
                                                + a slice, etc
'''

labeled_alphabet = pd.Series(data=list(ascii_lowercase), index=map(lambda x: 'label_' + x, list(ascii_uppercase)))
print(labeled_alphabet.loc['label_V'])
# now using a callable we can write
print(labeled_alphabet.loc[lambda x: 'label_V'])
# So above, we have 2 differents approcah 1/ classic 2/ with a callable producing the same result

print(labeled_alphabet.loc[lambda x: ['label_V', 'label_A']])

print(labeled_alphabet.loc[lambda x: [True for i in range(x.size)]])


def every_fith(x):
    return [True if (i + 1) % 5 == 0 else False for i in range(x.size)]


print(labeled_alphabet.iloc[every_fith])
