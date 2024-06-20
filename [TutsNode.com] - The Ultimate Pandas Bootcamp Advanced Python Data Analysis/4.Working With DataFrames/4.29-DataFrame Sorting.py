# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames
import io
import pandas as pd
import requests
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 9000)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col='name')  # we position the index column on name column

nutrition.replace('[a-zA-Z]', '', regex=True, inplace=True)
print(nutrition.head())

nutrition = nutrition.astype(float)


'''
Now that we have a numerical data frame, we are free to apply all the methods and functions that we 
we have discussed in series section.
It will be meaningful now to see this in action.
Let's begin with sorting, wich is something we explored before using series for a quick review of that.
Let's get a serious by picking one of our data frame columns here.
I'll say nutrition dot vitamin B12 maybe. And this serie can verify by looking at type.
'''
print(nutrition.vitamin_b12)

'''
And this series can be verified by looking at type.
'''
print(type(nutrition.vitamin_b12))

'''
So now in order to sort this, we simply say sort heights.
So we now get a series that is sorted in ascending order.
'''
# print(nutrition.vitamin_b12.sort_values())

'''
Note the syntax for DataFrames looks identical to the entire nutrition data frame.
We say nutrition dots are values.
But now it won't work without passing, at the very least, an argument to the pi parameter.
Let's think about why this is for a second.
When working with series, we have a single sequence of values, right?
We were working with only one column.
So if we say sort values, pandas knows exactly what to sort.
There's no possible confusion because there is only one column.
In a DataFrame, we have an additional dimension, which is the column axis.
And so if we say surge values and we just leave it at that, there is some anbiguity, there is uncertainty
over what exactly do we want to sort by, because our DataFrame contains several columns, each of
which has different sequences of values, which understandably will result in different sort orders
to avoid this uncratainty. We'll say that we want to start by caloric content, by calories here.
So let's say certain values and to the by parameter, I'll pass Pythonesque
containing a single label called calories. And let's do it in descending order as well.
'''
#print(nutrition.sort_values) this does work because of the explanation above
print()
print(nutrition.sort_values(by=['calories'], ascending=False).head())

'''
Let's talk about something else, maybe cholesterol and sodium
Perhaps studies indicate that these two are correlated with heart disease.
So let's see what foods have the most cholesterol and sodium.
Now we are going to see something that we haven't seen thus far 
Cholesterol mg, sodium mg And that is sorting by two columns at once.
This is obviously something that we could only do in a DataFrame and we'll set ascending to false.
And in order to get the largest numbers up top again. And let's give this a go.
'''
print()
print(nutrition.sort_values(by=['cholesterol', 'sodium'], ascending=False).head())

'''
By the way, now that we're working with data frames and sorting by mutliple columns, we also have 
the option of sorting in different directions.
So we could start by cholesterol in ascending order and sodium in descending order, by passing a python list
to the ascending parameter, which means, therefore, boolean false.
We can pass a python list containing multiple booleans.
So if we say true or false here, we're saying cholesterol needs to be in descending order.
In other words, if sending false and sodium needs to be in ascending order.
So it looks like not much changed, but now cholesterol continues to be the highest cholesterol foods
continue to be ranked up top. 
And then as a second consideration, we are storying by sodium in reverse order.
So that's the only thing that changed.
'''
print()
print(nutrition.sort_values(by=['cholesterol', 'sodium'], ascending=[False, True]).head())

'''
So it looks like animal brain has the most cholesterol and sodium.
Although surprisingly, it doesn't have that much fat.
'''
