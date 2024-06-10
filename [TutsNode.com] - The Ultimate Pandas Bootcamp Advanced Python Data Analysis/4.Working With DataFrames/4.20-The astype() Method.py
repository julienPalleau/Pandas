# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
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
Pandas has a very useful built in method that help us cast a given data frame or series from one data type to another.
Well, first, explore this method in isolation and then we'll see if we could use it to clean up our nutrition data frame and convert
those strings to ingegers.
Let's creating a data frame here containing three columns with four values each.
So again, we have the data frame convstructor here, and we're passing in a python dictionary containing three keys.
These are the column labels, as well as three python lists with different values.
The age column is going to contain four integers, as we see here.
The weight column for floating point variables and the height column for strings.
'''
df = pd.DataFrame({
    'age': [12, 13, 14, 16],
    'weight': [41.1, 34.5, 83.2, 90.1],
    'height': ['1.73', '1.74', '1.91', '1.54']
})

'''
So our data frame here contains three columns of different dtypes. We can confirm that by lookint at the info method on the df.
'''
print(df.info())

'''
We see int, float, and object. That's our string based column height here.
So now let's use the as type method to convert all of these columns into one common dtype.
Let us go with float to begin with.
So we say df astype() and then float.
Do we see a change here? Let me bring up the original data frame up here.
So what is the difference here? Well, our H, which was an integer now looks like a float. 
We got these decimal component going on here.
We could confirm this by also looking at the info again, again, again, say D.F. info.
'''
print(df.astype(float))

'''
Looks like nothing has changed here, and that's because as type is one of those methods that returns
a copy of the data frame. It doesn't have an inplace parameter.
'''
print(df.info())

'''
So in order to modify the original data frame, we'll have to reassign it or we assign this copy to the df variable.
So now if we go back to df info, we see that everything has been cast to floats.
'''
df = df.astype(float)
print(df.info())

'''
The ask type method is also flexible in that instead of targeting the entire data frame like we're doing here.
It also allows us to modify only a subset of the columns.
So we could say, for example, that instead of everything as float, we want our age column to be integer.
So we say we pass in a Python dictionary as type and then we specify the column label as well as the intended data types.
In this case, I'm saying that age means to be an integer.
'''
df=df.astype({'age': int})
print(df.info())

'''
My way this works with python types or numpy dtypes. So we could cast the age, for example, sixteen bit numpy integer.
So we say numpy and 16.
So same syntax and the same effective output, but different memory implications. We're using a different type here.
'''
df = df.astype({'age': np.int16})
print(df.info())

'''
But is this all we need to solve our problem, the prolbem that we have with our nutrition data frame?
Let's take a look at that. I'm going to bring up a small chunk of nutrition here. Let's say the first.
So, I'm going to say the first four rows and all the columns. And then I'll attempt to cast all of these two flot.
So I'll say as type float. However as great and flexible as the astype() is, unfortunately it is not the silver
bullet for our problem because these constructor's cannot handle nonnumeric input very well.
It looks like we're going to have to first get rid of the units from each string, as in strip, each 
value of its units, spearate them. For example, remove the G from seven, one from G.
In the next lecture, we look at exactly how to do that.
'''





