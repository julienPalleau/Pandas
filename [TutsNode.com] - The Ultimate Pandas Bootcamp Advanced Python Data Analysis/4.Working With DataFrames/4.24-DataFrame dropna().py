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
age = [12, 13, 14, 16]
weight = [41.1, 34.5, 83.2, 90.1]
height = [1.72, 1.74, 1.91, 1.54]
df = pd.DataFrame({'age': age, 'weight': weight, 'height': height})

'''
Let's talk about applying an old method to a new context, we saw in working with series that the dropna() method excludes all null values from a given 
series and indeed frames. It does exactly the same. But it comes with a few additional powers, most importantly, with data frames.
We could specify the access we want to draw from. It's a good some examples here. 
And for this will bring back our toy data frame, which we called df. Remember, it has four rows and three columns and currently does not have it
does not contain a null value. So let's start by answering one said df lock to select a row labeled two and then wait to select that column.
And let's insert another. Take a look at the data frame. And sure enough, it now has a gap.
Perhaps it's also change an entire role. Sorry to say, does long on to select their own labels one and then call in to select
all the columns and np.nan again, I am using numpy not a number object.
'''
df.loc[2, 'weight'] = np.nan
print(df)

'''
Now let's set an entire row to nan.
So at this point, we have a data frame that has at least one and nan in each column.
And at least one nan in two of its four rows.
'''
print()
df.loc[1, :] = np.nan
print(df)

'''
Let's see how drop and he behaves with data like this.
We'll begin by specifying the method with no arguments.
What we get back is a data frame that exclude all rows, which contain at least one nan.
So they're all for index one, which contained all only nans is gone.
And so what is the role of index two which contained a single nan for weight?
The only raws remaining are those labeled 0 and 3, which contain no nan at all.
'''
print()
print(df.dropna())

'''
Now, it would be a bit restrictive if you drop and they always work like this.
And fortunately, that is not the case. 
There are two parameters which are currently set to their defaults which drive this behavior.
Using drop nan without any arguments, as we are doing here, is the same as saying drop nan with the how
parameter set to any and the axis set to zero.
'''
print()
print(df.dropna(how='any', axis=0))

'''
The axis parameter above is used to indicate the dimension or access through which we want the method to operate in defaults
to zero, which is the real axis.
And that means that we want that drop any method to exclude rows instead of columns, the how parameter on the other hand,
specifies the condition under which the method applies. 
When we say any, we mean that the sequence of values, being a row or a column, depending on the 
access we specified, should be dropped in it entirety if any of its values is nan.
That's why both the row index one and two are excluded because two has a single one and one has more than three names.
And so they meet this criteria of any. And so they're dropped.
'''

'''
Another possible value for the how parameter is all when we say all, we indicate that only the rows where all the values are nan, should be excluded.
So if we set how to all and again the access to zero.
Now we're saying that only rows where all the values are nan are dropped.
And sure enough, a one is dropped, but two which has a single nan is not excluded.
So the how parameters allows only these two options: any or all.
'''
print()
print(df.dropna(how='all', axis=0))

'''
There is, however, another value that allows us to fine tune is dropping condition.
If we could call it that. And that is to use the thresh parameter after it is short for threshold.
And it gives us an opportunity to specifically say how many known and a values we want in a given sequence.
It could be, again, row or a column for that to be included in the resulting data frame.
So this is a bit of a reverse condition, whereas with the how parameter, we specify exclusion criteria,
in other words, conditions for what should be dropped or excluded with the thresh parameter.
We define an inclusion condition.
We're not specifying the minimum number of non any values for the records that we want to be included.
So we say the df.dropna(), thresh, three and axis is zero.
So we're seeing that in the resulting data frame. We don't want all null rows.
Remember axis zero that had at least three non nan values.
'''
print()
print(df)
print('debug')
print(df.dropna(thresh=3, axis=0))

'''
By the way, because our data frame only happens to have three columns, this is the same as saying 
df dropna(how='any', axis=0)
In bot cases,we have no tolerance for any nan values.
'''
print()
print(df.dropna(how='any', axis=0))

'''
As an additional bonus point, we could generalize this condition using thresh by saying something like,
you have to drop nan thresh df shape one, axis zero.
'''
print()
df.dropna(thresh=df.shape[1], axis=0)

'''
So in here, we're saying that we want these dropping additions to be applied to the row axis. So we want the rows to be excluded.
And as a threshold for non na values is set to the maximum.
So we want to have as many non nan values as this data, as there are columns in this data frame.
Remember, the shape object for data frames is a tuple that contains two values, the length of the 
rows, the axis, the index axis, as well as the length of the columns.
Now let's play with this axis parameter. If we say df, dropna() axis one.
We got an empty DataFrame with an index but it has no column why is that?
Well, that's because the how parameter defaults to any and our original data frame has nan in all columns
'''
print()
print(df.dropna(axis=1))

'''
So how many axis?
So the one above and the one below are equivalent
'''
print()
print(df.dropna(how='any', axis=1))

'''
Now if we switch these back to all, we get everything back because our data frame does not contain any
columns. Where all the values are nan.
Each column in our DataFrame has at least one, not any value. And so everything is returned.
'''
print()
print(df.dropna(how='all', axis=1))

'''
Obviously we could also combine thresh with the column axes.
For example, we could use thresh specifying a threshold of three.
You know, any values and we now see that the weight column has been
dropped because it did not meet the threshold requirement.
The weight column has two non nan values the first and the fourth.
Whereas our threshold is set to three. And so the conditions is dropped. 
'''
print()
print(df.dropna(axis=1, thresh=3))

'''
In conclusion, dropna() is a very poserful and widely used method to clean up our DataFrame by specifying
conditions on na and nan across the index and column access.
While this thing to note is that everyting we did in this lecture returns a copy of the data frame.
So all of these DataFrames are copies of a df.
The df remains unchanged.
'''
print(df)

'''
But the drop any method is one of those methods that supports in place parameter.
So if we set in place to true. Sure enough, the change will carry.
'''
print()
print(df.dropna(axis=1, thresh=3, inplace=True))
print(df)
