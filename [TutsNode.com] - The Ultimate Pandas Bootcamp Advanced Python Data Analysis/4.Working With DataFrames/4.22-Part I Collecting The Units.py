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
At the end of the previous lecture, we said that it might be a good idea to extract the units from
each column and then embed them into the column labels up here in this lecture.
We'll take the first step towards doing that by first isolating the units themselves.
By the way, all of this might feel a bit tedious or too challenging at this point.
In fact, I selected this data set on purpose so that we could get some practice with the kind of problems
that you might run into when working with real world data.
It's almost never the case that you'll get pefect quality data right from the start.
More often than not, there will be a lot of cleanup and transformation involved.
How are we going to isolate the units?
Well, start simple by first removing all the numeric values from our dataset.
Anything that is not a unit needs to go. If we remove all the numbers. 
The only thing remaining will be the units.
One way to remove the numbers is to use the replacements it with regex pattern that identifies
the number portion of each string and then replace it out.
So let's set that up by applying the replace method. I mean, the nutrition data frame.
Before we decide on the pattern, let's pick a set of her random units from our data frame.
'''
nutrition=nutrition.replace('[^a-zA-Z]', '', regex=True)

'''
I'll use the sample method here to select some columns
so we have a sample here.
See more units we were dealing with grammes, mili centigrams, mg
'''
print(nutrition.sample(20, axis=1).head())

'''
Let's run another sample.
'''
print(nutrition.sample(20, axis=1).head())

'''
Seems like we got back a data frame where only the year is remaining.
But there is a strange thing here in that calories continues to live on as untouched by this replacement.
The reason is that rejects because it's a sting manipulation technique and domain specific language.
It only targets strings columns, but caloris is numeric. I believe we saw that it was an integer series.
So it is not affected by regex. There's a couple ways we could handle this.
But perhaps the easiest is to deal with it right now by casting the entire series to string.
So this step converts all of the columns in our data frame to a string, and then that way they're all affected by regex.
So if we re-run this snap.
We are going to see that calories is also gone, no calories is an empty column now.
So at this point, we have a data frame of units only.
It's a couple of gaps, though, some NaNs emtire blank columns like the universe called callories
because there's gaps and our data sometimes includes units and sometimes not.
We have to figure out a way to get the appropriate unit from each column.
'''
units = nutrition.astype(str).replace('[^a-zA-Z]', '', regex=True)
print(nutrition.sample(20, axis=1).head())

'''
Let's look at some example here.
I'll begin by assigning these to units so that we have a nice handle.
So let's look at a couple of examples here.
So the first five examples from our units, from our new units, data frame out of these five observations,
we see two nans and three g in the saturated fat column.
'''
print()
print(units.head())
'''
We know that the right unity's g for grame.
But how do we figure this out at scale?
How do we manage to do this for all our columns?
I think it's obvious that we cannot just pick or roll because of these unpredictable gaps.
The first row doesn't have a cholesterol unit, for example, but the fourth row, which may have or
the fifth row, which may have a cholesterol unit, has a gap in another column like perhaps folic.
So it is not reliable to just pick a column at random because we are bound to run come across one of these gaps, you know, in relatively unpredicatable ways.
So one nifty workaround, one solution to that would be to find the mode unit from each column.
Remember in statistics, the mode is the item that shows up the most frequently in a set of values.
So if we look at saturated fat in isolation and we're selecting a single column, so we get a series
and then we can use the value counts method on these series.
We get a count of all the unique values in that series.
'''
print()
print(units.saturated_fat.value_counts())

'''
So we see that there's about 1600 nan from food that contain no saturated fat at all.
But the most common value is g. And that's exactly what we want.
We want gramme to be the unit for the saturated fat column.
Now, how do we pick the most common value from each of these columns?
We could simply use the mode method when we apply mode to a series.
So units, saturated fat target mode when we apply mode to a series.
We got another series containing the most common observation when we apply mode to a data frame like units like mode.
We get another data frame with a single row containing the value that shows up the most frequently in each column,
which is amazing because it aligns very nicely with what we were looking for.
Notice how we now only have the units from each and every column in our data frame.
'''
print()
print(units.mode())

'''
Lastly, how to reassign this data frame to point to the unit's variable C units mode.
'''
units = units.mode()
print(units)