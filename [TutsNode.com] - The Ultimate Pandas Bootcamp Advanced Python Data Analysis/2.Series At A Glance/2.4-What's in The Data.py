# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas as pd

books_list = ['Fooled by Randomness', 'Sapiens', 'Lenin on the Train']
list_s = pd.Series(books_list)
print(list_s)

books_dict = {0: 'Fooled by Randomness', 1: 'Sapiens', 2: 'Lenin on the Train'}
dict_s = pd.Series(books_dict)
print(pd.Series(dict_s))

'''
List argument:
pd.Series(data=['this', 'is', 'fun'])

Dict argument:
pd.Series(data={0:'this', 1:'is', 2:'fun'})

Also valid series:
pd.Series(data=0)   pd.Series(data='weather')
'''
