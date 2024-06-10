# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io

import pandas
import pandas as pd
import requests
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 50)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col='name')  # we position the index column on name column

'''
Before we proceed, we will spend the next couple of lectures exploring two methods which will help
us with our data frame transformation. 
The first method will come in handy very soon, but it's also almost universally useful when working with pandas and data in general.
That is the rename method using rename will be able to essentially change or rename our labels.
Remember, our data frame has two labeled dimensions. The index and the columns.
And using the rename method, we could change either or both of them.
As always, we will first explore this method in isolation before we use it at scale.
Later in this section, I'll pull up a sample data frame, which we created a couple of lectures ago called df
We call that this data frame had three columns containing the age, weight and height of four unnamed creatures.
'''
data=[[12.0, 41.1, 1.72], [13.0, 34.5, 1.74], [14.0, 83.2, 1.91], [16.0, 90.1, 1.54]]
df = pd.DataFrame(data, columns=['age', 'weight', 'height'])
print(df)

'''
Now, if we want to rename our index labels here, we could say the df rename index.
So we passed this dictionary, this dictionary acts as a map of values, specifically mapping the current label.
Represented by the key here to the label that we want to rename it to.
In this case, the string Pikachu. So we're saying replace zero with Pikachu.
Let's run this.
And we see that we have changed the label for the first row from the integer zero to the string that we specified.
We could do something similar with the next row and copy this to the next cell and to modify the next row.
We can simply add another key value pair to this dictionary. Let's say I'm the second creature.
'''
print(df.rename(index={0:'Pikachu', 1:'Andy'}))

'''
So far, we've seen renaming the index axis. In order to rename our column labels, we simply pass a dictionary to the 
columns parameter instead.
So we say df rename columns instead of index passing a dictionary again.
The syntax remains the same. And in this case, it's rename weight to capital weight.
'''
print(df.rename(columns={'weight': 'Weight (kg)'}))

'''
And of course, we could do both axis at once.
So both the index labels and the column labels all in one go, for example.
So tow columns we passed this dictionary to index, we can simultaneously pass another dictionary.
'''
print(df.rename(columns={'weight': 'Weight (kg)', 'height': 'Height (m)'}, index={0: 'Pikatchu'}, inplace=False))

'''
By the way, the renaming that we have done so far did not stick around because we didn't do it in place.
In each case, a copy of the data frame was returned.
So we still have the original data frame, df with unchanged labels.
'''
print(df)

'''
Three rename supports the inplace parameter, which defaults to false, and I will not change it for now.
An alternative approach is to simply pass a dictionary that maps the old labels whith new ones to a parameter
called Mapper. So we could say the F rename mapper. And then we pass let's pass
When we run this we don't actually get an error, but notice that nothing happens either.
There no renaming going on. The reason is that our method, call here is a bit ambiguous because we're never using mapper.
'''
print()
print(df.rename(mapper={'height': 'Height (m)'}))

'''
We have to be specific about which access we want the map here to apply to in our previous examples.
We specify either columns or index. So there was no confusion, no ambiguity.
But with Mapper, there is by default access zero. The index access will be renamed.
And that's because there's a parameter here called indexe that defaults to zero.
But there's no index label called height. And so the method replaces nothing.
No replacement takes place.
How do we specify that we want this mapper to act on our column labels?
We simply change the access parameter from zero to one.
Soo now it's renamed the catch here is that when using mapper, we couldn't we 
would not be able to rename both the column and the index axes at once,
because this access parameter here could either be zero or one, 
but not both at the same time. 
There's just something to be aware of it we're trying to rename both axes, both dimensions.
At the same time, we would be forced to use a syntax like this that explicitly assigns to the columns
and index parameters. 
'''
print()
print(df.rename(mapper={'height': 'Height (m)'}, axis=1))

'''
And by the way name raws instead of zero or columns instead of one to the access parameter works just fine
'''
print()
print(df.rename(mapper={'height': 'Height (m)'}, axis='columns'))

'''
This goes for other pandas methods that support the access parameter.
I personally prefer the integer based notation because it ties nicely with other concepts in Pandas.
For example, if you look at df.axes, one, we get the column axis, and that is y axis one here refer to columns.
'''
print()
print(df.axes[1])

'''
Similarly, the axis, the df axis zero gives us the index labels, and that is why
axis zero here refers to the raws.
'''
print()
print(df.axes[0])

'''
So I prefer this because it really ties very nicely conceptually and honestly. And it's less typing it is shorter.
'''