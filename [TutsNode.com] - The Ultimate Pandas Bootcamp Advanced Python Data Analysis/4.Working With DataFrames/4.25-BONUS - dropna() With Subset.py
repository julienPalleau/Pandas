# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import pandas as pd
import numpy as np

'''
BONUS - dropna() With Subset
'''
age = [12, 13, 14, 16]
height = [1.72, 1.74, 1.91, 1.54]
df = pd.DataFrame({'age': age, 'height': height})
df.loc[1, 'age']=np.nan
df.loc[1, 'height']=np.nan

'''
Remember, it's now a smaller dataset because we dropped some na in place at the end of the previous lecture.
So this is all we're looking at right now.
We go ahead and add a new column. I'll add gender and set it to a list of values
'''
df['gender'] = ['M', 'F', np.nan, 'F']
print(df)

'''
So if you take a look at the data frame now, we notice that we have a new column and this new column
has a nan value for the roll labeled too.
So if we now run dropping in on this new data frame, we see that the rows labeled one and two have
been removed have been dropped.
'''
print()
print(df.dropna())

'''
And for a quick review, what we're doing here is we're seeing dropna() and Axis zero
So these are the defaults. Obviously the results are the same because rows one and two each have least one nan. 
how is set to any so they are both removed.
'''
print()
print(df.dropna(axis=0, how='any'))

'''
Now, so far argues of dropping it has impacted the entire data frame.
We called the method on the DataFrame itself, df, to drop in it, and it is applied to all of its 
rows and columns.
In this lecture, we'll introduce the subset parameter, which gives us a way to restrict drop any to
only a handful of row or column labels that we choose. So the subset parameter. 
'''
# the subset param
df.dropna(axis=0, how='any', subset=['gender'])

'''
What happened above? Just like 2 steps above we said drop all rows axis 0 which have at least 1 nan. how=any
But now only look at the gender column to make this determination.
So by using this subset parameter, we're telling pandas to turn a blind eye to all the other columns
in this data frame and only look for names in gender.
And sure enough, the only rule that is removed is the third one.
And the reason is because it is the only row that has a nan in the gender column.
So that's what subset does in a nutshell.
If we change this up a bit and specify H, and copy to your line for clarity, say age instead.
What do we expect?
Well, now, because age has a nan in the row with the index label one and not nan values everywhere else.
We expect to get three rows back, not including one. Remember, our df looks like this.
'''
print()
print(df)
'''
if we subset it,if we started dropping it to only look at age, it will exclude this row.
'''

'''
So far, we've been working with row the axis.

It looks like nothing is returned and it's because all of our columns have at least one nan.
'''
print()
print(df.dropna(axis=1, how='any'))

'''
Using the subset parameter we could mitigated some bit by specifying a list of index labels and taling
drop nan to only look at those instead.
One key thing to remember here when using subset is that we are expected to always specify labels that
are orthogonal to our main axis. World of lecture where the lecture is orthogonal. 
So previously we had axis zero. Which is the index, and so we gave subset column labels.
Because now our drop in access is one. The subset parameter will take role labels, index labels.
I'll start by saying 0 and 2.
And before we run this, let's take a second to think about what we would expect.
'''
print()
print(df.dropna(axis=1, how='any', subset=[0, 2]))
'''
Now, put the DataFrame up here for our reference, and let's work through this step by step.
'''
print()
print(df)

'''
So we have axis one which means that we want to now drop columns and we have set the whole parameter
to any which means that we want to drop columns if they have at least one nan. 
And finally, our subset is set to zero and two, which means that we only want to consider the rows
labeld zero and two when making this determination on what to draw.
So what do we expect to be dropped?
Well, the roll with the index label zero contains no nan, and so no column is dropped because of it.
Whereas the row with the index label, too, contains nan in the gender column. And so the gender column is dropped.
So these results are consistent with what we expected here.
'''
print()
print(df.dropna(axis=1, how='any', subset=[0, 2]))

'''
            dropna() with subset
            
            
    df.dropna(axis=0, subset=['gender']
  drop rows                            but only look at gender
                age     height      gender          DF.DROPNA()
            0   12.0    1.72        M               removes columns or rows with
            1   NaN     NaN         F               missing values
            2   14.0    1.91        NaN             SUBSET
            3   16.0    1.54        M               restrict or localizes the method
                                                    application to specific
                                                    orthogonal labels
                                                    
It allow us to fine tune and localise the effect of drop nan to set a column or row level or a set
of labels that we specify that we want this method to be applied to.
'''