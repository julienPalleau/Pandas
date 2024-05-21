# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd
from string import ascii_lowercase, ascii_uppercase

labeled_alphabet = pd.Series(data=list(ascii_lowercase), index=map(lambda x: 'label_' + x, list(ascii_uppercase)))

# get()
print(labeled_alphabet.get('label_I'))
# in a sens .get() is very similar to .loc[]
print(labeled_alphabet.loc['label_I'])
# Both of these methods above are quite similare to full square brackets
print(labeled_alphabet['label_I'])
# => So the 3 lines above show 3 different approaches that give the same result
# So why use get() method when we have loc[] method and classical full squre brackets [].
# The get has some convenienties for instances what happens if we try to access a label that does not exist.
print(labeled_alphabet.get('label_Inexistent') == None)  # get support a default paramether which by default is assigned to None
print(labeled_alphabet.get('label_Inexistent', default="Could not find anything by that label, sorry."))
# default can contain a string, a dictionary, an integer a more globally an object.


