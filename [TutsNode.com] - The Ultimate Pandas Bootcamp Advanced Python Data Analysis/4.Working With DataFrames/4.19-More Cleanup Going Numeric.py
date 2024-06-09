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
If we look at our data frame right now, nutrition head. We noticed that in its current structure, even though most of it looks
quantitative and numbers based, it's actually not really conclusive to numerical analysis, because all of these
columns that contain units, they're actually strength. 
'''
print(nutrition.head())

'''
For example, if we look at total fat nutrition, total fat, .head.
We see values like 0.1g. Now we understand that 0.1g plus 72g 
But to pandas these are just strings. 
'''
print()
print(nutrition.total_fat.head())

'''
So if we try to hide them instead of a numerical sum, we end up getting a long concatenated shrink
surfacing nutrition, nutrition and total fat. Something we get this really long string.
So not exactly what we're expecting here.
'''
print()
print(nutrition.total_fat.sum())

'''
And the reason this is happening is that we're applying the plus operator to a long sequence of strings.
It's as if we're doing this plus, but on larger scale with way more strings.
'''
print()
print("Andy" + "Beck")

'''
And of course, the plus operator is not an exception. Are their numerical functions also don't apply the way we really expect them
to? For example, Max, if we try nutrition model that not max a tree turns 90 when we know we have larger values.
I mean, we see 72 G here, you know, in this second observation.
But when we say max on total fat, we get 9g. The reason for that is that these are being compared as shrinks.
And 9, the first character of this shrink comes after seven. And so it's treated it has a larger a quote unquote, larger value.
So it's quite clear that before we begin to do any meaningful analysis on this data frame, we have to convert all the columns
that contain units, which as a result are strings to numeric columns. And by the way, we have to convert a lot of them.
'''
print()
print(nutrition.total_fat.max())

'''
It's actually most of our data frame. So when we look at nutrition info, we see that the issues we discussed here 
apply to most of our columns. We convert this to a non verbose output. So it's easier for us to process.
'''
print(nutrition.info())

'''
So we see we have 73 columns that contain strings, combining numeric values with units.
And we've seen the strings in pandas, data structures result in object dtypes, which is what se see here.
So how are we going to fix this? We'll do it in a couple of steps. 
But before we jump into it, let's discuss in the next lecture a common method used to cast series and
data frames from one data type to another. 
'''