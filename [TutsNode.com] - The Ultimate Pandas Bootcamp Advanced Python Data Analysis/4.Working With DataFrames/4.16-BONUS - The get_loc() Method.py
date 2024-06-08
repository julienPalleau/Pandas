# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
import pandas as pd
import requests

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 50)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col='name')  # we position the index column on name column

'''
As we saw in previous lectures, whenever we work with position based extraction approaches, we may
find ourselves counting columns or rows to figure out the exact integer location of the data we're interested
in, or when specifying a slice, the boundaries around the sequence of rows and columns we want to access.
These may especially be the case when we combine labels with positions. 
For example, say we're interested in figuring out how much vitamin K, the third for in our dataset has?
'''
# column label: 'vitamin_k'
# index position: 3
'''
Well, at this point we have a label, Vitamin K and a position three.
But as we saw in previous lectures, the loc and iloc attributes as well as their single value access counterparts.
The at and iat indexers, all of these approaches expect consistent indices.
In other words, they either expect labels or they need integer positions.
Which really leaves us with two options, we either figure out the index label for the third foot and 
the use a label based approach like loc or at or alternatively, we identify the column integer location
for Vitamin K, our own label, and then use a position based approach. 
Like I said in this lecture, we'll see how to do both. So that at the end of the day, we have argument that are,
Parameters that are propulsor.
Word of the lecture is propulsor, which means kind of equal, like on equal footing.
So that's the entire purpose of this lecture, when in cases where we have a label and a position, 
how do we get two labels or two positions?
Let's start with figuring out the label for the fird row.
Let's call this approach number one and get label from position.
We could start by isolating the index, so nutrition or index, that gives us the entire thing.
'''

'''
We know all we want to access the third food. So, I'm going to pass in an exposition to. So we get the label.
Are you signed to a new variable? I call it index label.
'''
# Approach #1 - get label from position
index_label = nutrition.index[2]
column_label = 'vitamin_c'
'''
And now that we have the label for the role, we could put together with column label and use the loc attribute
to complete the extraction sounds a column, a label is our vitamin K.
So now we have both piece of information two labels.
'''
print(f"get value at index_label, column_label: {nutrition.at[index_label, column_label]}")

'''
Another way to handle this it is to figure out the integer location for the label that we know Vitamin K.
So I'm going to call this approach number two, get integer location from a label.
And this is where the get lock method comes in.
'''

'''
Get lock helps us get an integer locatoin for a given label.
So it's kind of the definition of what we're trying to do here to use it.
We merely saying nutrition columns. 
'''
# Approach #2 - get int location from label
print(f"numero of column vitamin_c: {nutrition.columns.get_loc('vitamin_c')}")

'''
So this is the column location check column.
'''
column_loc = 23

'''
And we know that the index loc is three.
'''
index_loc = 2

'''
We were interested in the Fourth position. 
So now that we have tow integer locations, we can easily combine them nutrition, .iloc
'''
print(nutrition.iloc[index_loc, column_loc])
print(nutrition.iat[index_loc, column_loc])