# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd

books_list = ['Fooled by Randomness', 'Sapiens', 'Lenin on the Train']
list_s = pandas.Series(books_list)
books_dict = {0: 'Fooled by Randomness', 1: 'Sapiens', 2: 'Lenin on the Train'}
dict_s = pd.Series(books_dict)
book_series = list_s
print(book_series)

'''
What is the difference between an attribute and a methode
    An attribute is a variable boud to the object: books_series.size size is an attribute, list_s.dtype dtype is an attribute
    A method is a function bound to the object: list_s.equals(dict_s) equals is a method
'''

'''
Let's talk about name attribute
'''
print("name attribute is pointing to NONE object")
print(book_series.name == None)
book_series.name='my favorite books'
# We can see with the line below that we now have a name for the series
print(book_series)

# What's the point of this as we will see later when we introducte data frame the name of the series
# becomes the column name in the data frame

'''
To summarize:
Series have name and those become column names in data frames.
Just like the series itself the series index could also have a name of it's own.
'''
print()
print(book_series.index.name==None)
book_series.index.name='My books'
print(book_series)