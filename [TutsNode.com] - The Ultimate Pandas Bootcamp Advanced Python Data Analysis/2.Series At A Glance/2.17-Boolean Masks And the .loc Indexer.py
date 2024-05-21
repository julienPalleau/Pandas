# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

labeled_alphabet = pd.Series(data=list(ascii_lowercase), index=map(lambda x: 'label_' + x, list(ascii_uppercase)))
# regular way (less efficient than loc)
print(labeled_alphabet['label_F': 'label_J'])

# loc (It is always better for efficiency to use loc and iloc rather than the regular way)
print(labeled_alphabet.loc['label_F':'label_J'])

# boolean
books_list = ['Fooled by Randomness', 'Sapiens', 'Lenin on the Train']
book_series = pd.Series(books_list)
print(book_series.loc[[True, True, True]])
print(book_series.loc[[True, False, True]])

print(labeled_alphabet.size)
print(labeled_alphabet.loc[[True for i in range(26)]])
print(labeled_alphabet.loc[[True if i % 2 == 0 else False for i in range(26)]])

'''
To Summarize
        Boolean Masks
+ used to index select items at scale
+ work with [] and .loc
+ need to same length as series

pd.Series(['A', 'B', 'C'])[[True, False, True]]
    0 A
    2 C
    dtype: object
'''