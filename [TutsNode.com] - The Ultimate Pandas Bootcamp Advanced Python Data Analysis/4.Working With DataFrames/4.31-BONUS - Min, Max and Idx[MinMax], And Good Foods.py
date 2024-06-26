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

'''
In the series actions, we reviewed the mean max, as well as the idea it's been an idea it's max methods
which are used to give us the labels associated with a minimum and maximumn values.
And the good news is that four data frames, these two work almost exactly the same way, except 
they now support an access parameter, because we can technically find a minimum of all columns as well as whole rows.
Like row wise minimun's or colonialized minimum's.
The default is to find the column wise one.
So, for example, if you say nutrition mean, that is going to return a serie where each label is 
accountable and each value is the minimum registered along that column. 
If we want to flip this on its head to relies so horizontally.
All we have to do is switch the axis parameter from its default of zero to one.
And sure enough, we now get minimum's across each row.
For example, Cornstarch zero.
'''
nutrition.replace('[a-zA-Z]', '', regex=True, inplace=True)

# Let's convert all the values in float in order to sum them up.
nutrition = nutrition.astype(float)

mins=nutrition.min(axis=1)
print(mins)

'''
Apparently all of the foods out there are most of them at least have a micronutriment that is zero.
And therefore, the minimum. So the max works very similar to that. 
Sam, the only distinction, the only difference between the series and a data frame min max is that
now we have two dimensions to apply the minimum, the maximum function to it, and therefore we have
more to specify in the method.
And the other distinction is that obviously we now don't have a single value, but rather many minimums
and many maximums, as many as there are columns or rows, depending on which axis we're applying this
method to. Now, is there something more practical? 
Let's say we want to figure out what the maximum amount of potassium, what food has the most postassium.
We are trying to answer these analytical question.
Well, we could simply say nutrition, potassium.
'''
print()
print(f'maximum potassium: {nutrition.potassium.max()}')

'''
If we're wondering what food as this we could use the idxmax method to identify the
label associated with its maximum value.
Well, you know, nutrition, potassium idxmax.
'''
print(f'food containing the most potassium: {nutrition.potassium.idxmax()}')

'''
Let's look at a couple of more.
sort values and I'll do it in descending order so that we get the mixed numbers up top.
'''
print()
print(nutrition.potassium.sort_values(ascending=False).head(10))

'''
So a couple of things here we have spices, celery and some instant beverages, surprinsingly.
Now, I'm not a nutritionist, but from what I've read, the right way to view dietary potassium is 
in relation to the amount of sodium in the diet.

Let's try to do a proper back of the envelope calculation of this ratio with our food items in our dataset. 
So let's we're targeting potassium to sodium of 16.
Ok, now let's create a series on the fly by dividing our potassium column by the sodium line so that
'''
print()
K_to_NA = (nutrition.potassium.replace(0, 1)/nutrition.sodium.replace(0, 1)).sort_values(ascending=False)
print(K_to_NA.head(10))

'''
But what kind of foods sit right around that golden number that our ancestors used to average?
So to answer that from the series we created up here, a K_to_NA we can.
To do some indexing using the between method, which we recently learned about so we can say between
14 and 18. And let's sample some foods from their.
'''
print()
print(K_to_NA[K_to_NA.between(14, 18)].sample(10))