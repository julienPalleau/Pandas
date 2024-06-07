# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
import pandas as pd
import requests

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',50)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col=0)
print(nutrition.head())

'''
We mentioned how data frames have two dimensions, and visually, these are let's print the first couple of records here as a reference.
So visually, these two dimensions are the indexable are the rows and the columns.
And again, conceptually, by data frames having two dimensions, we mean that the number of attributes that we would need to specify in order
to select a specific observation in our data frame is to. We need to provide the exact AROLE label, as well as the corresponding column label,
kind of like the coordinates of the datapoint. And these are known as data frame axes. These two dimensions. And we have easy access to both.
By using the access attribute, so we say nutrition on access. 
This returns a python list of two pandas index object, one characterizing rows this in 64 index here and the other columns.
This may be a bit too dense to process visually.
'''
print()
print(nutrition.axes)

'''
So let's look at this in isolation. Let's start with a first. That would be the wrong axis, we asxis it as simply the first item of his Pythonesque.
And maybe from that, we can even extract. The Third World label camp, byt way, this is completely equivalent to more directly saying nutrition dot
index three. 
'''
print()
print('---')
print(nutrition.index[3])

'''
The next dimension is Eikon levels. In other words, the second item in this Pythonesque of index is Hennessey's.
And that these are common labels. Again, extraction works very similarly. 
'''
print()
print('---')
print(nutrition.axes[1])

'''
So in order to source the sixty-nine column, which is say that.
'''
print()
print('---')
print(nutrition.axes[1][69])
# or
print(nutrition.columns[69])

'''
So these are the axis of our data frame as we progress in our usage of Pandas and deepen our data analysis toolkit.
We will inevitably see many methods in pandas that contain an axis parameter, the axis param. This shows up in a lot of methods.
For example, the first parameter of the drop in name asset, which will explore very soon, is access.
And it takes the integer zero or one. For columns or rows specifically, so zero indicates rows and one indicates columns by weight, it
also takes rows or columns as streams. But I wanted to talk about this integer based equivalence here.
'''
print()
print('---')
print(nutrition.dropna(axis=1))


'''
So if we say not only the drop in name method, but in any method that supports the axis parameter, when we say zero, that means row.
And when we say one, that means columns.
And recall that corresponds to the position of each index in our access Pythonesque.
So when we said nutrition acts is zero, we got back the role, the role labels.
'''
# the axis param
print()
print('---')
print(nutrition.dropna(axis=0))
# 0 => 'rows'; 1 => 'columns'
print()
print('---')
print(nutrition.axes[0])

'''
And when we said one got back the column labels. So this is just a nice mnemonic to help us remember this correspondence.
Most methods, with support, both the integer base and the string bass. 
'''
