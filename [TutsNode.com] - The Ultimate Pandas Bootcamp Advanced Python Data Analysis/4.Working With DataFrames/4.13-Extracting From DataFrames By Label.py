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
# therefore, we can coment out the line 36 - nutrition = nutrition.set_index('name')  # we put the column name as index

'''
When we talked about the series, we saw many ways to extract records. We discussed the lock and I lock indexers, square bracket indexing, direct
attribute access using dot notation, as well as the get method.
The good news is that all of that and more works for data frames to even better news is that because 
we now have two dimensions, we have even more power and options to slice and extract, because we could
do so along both rows and columns. Let's start with extraction by label in this lecture, using the lock attribute, which remember is 
the prototype away to extract by label in pandas. I've printed out the first five records below for a reference.
'''
print(nutrition.head())

'''
And now let's say I want to access this hack planned raw row here. Because we're now using the name calling as the data frame index.
I could simply say nutrition dot log and then specify the label for that role.
So the syntax here is almost identical to what we saw for series extraction by label.
But now, instead of a single value, we get back a sequence of values or a series slice it stikinkier is a series.
So if we pass it to type, we see that it's actually a Pandas series.
And this series represents all the column values for the eggplant row.
So it's as if we're selecting this entire sequence of values if we want to only look at ones of these fields.
Say, for example, eggplant calories. We have to further extract from this series. 
'''
# nutrition = nutrition.set_index('name')  # we put the column name as index
print(nutrition.loc['Eggplant, raw'])
print(type(nutrition.loc['Eggplant, raw']))

'''
And one way to do that is to chaine two square brackets.
So we say we first select eggplant raw and then further we select calories.
Now we have 25 representing the number of calories for this food item.
'''
print(nutrition.loc['Eggplant, raw']['calories'])

'''
But perhaps even better, we could do this selection at once.
By extracting along the row and column axes in one go.
So we could say nutrition block.
So we say eggplant raw and then , calories
So the lock indexer for data frames accepts two arguments.
Think of the first as specifying the labels, the "raw" labels that were interested in.
And the second argument as specifying the labels that we want from the column axis.
'''
print(nutrition.loc['Eggplant, raw', 'calories'])

'''
We also get more creative and provide slices instead of single arguments or single labels rather,
and this would work for Rose Collins or both.
So, for instance, if we want and say, what do we want here, they say we want 
the bottom three observations.
So the third, fourth and fith, and let's say on the columns front, we want everyting from calories to cholesterol.
So let's pass that to the loch indexer has a slice.
So it's a goal from eggplant Royale to Sherbet Orange.
'''
print(nutrition.loc['Eggplant, raw':'Sherbet, orange'])
'''
So this specifies narrow slice and then I'll say comma on the column front, go from calories to cholesterol.
As we see when we slice it long, both rows and columns, instead of series like we got abobe here.
'''
print(nutrition.loc['Eggplant, raw':'Sherbet, orange', 'calories':'cholesterol'])
'''
We get back a data frame, which makes sense because we are providing a range of values along two dimensions.
'''

'''
Yet another indexing technique is to provide sort of slices, as we're doing above, which gets us consecutive labels.
We could pass in a list specifying exactly the rows and columns that we were interested in.
So example nutrition log and then UPS. 
Let's start with raspberries and let's say on O'Collins, I want a protein, I know they don't have a lot of protein and I don't know, like vitamin B6.
So I tried to select raspberries from their row labels and I went from the columns. I want protein and vitamin B.
I'm using this technique here because these two labels are not consecutive. And so we cannot specify using a slice.
So now we get a new data frame that contains both of those columns which specify. Notice how we're kind of building our own little data frame here.
Step by step by specifying the row and column labels that we want. 
If I wanted to add to this, say, for example, I also want to figure out what happened here.
If I wanted to specify water as well. And if I wanted to add Blackberries as well so we can get a quick comparison going.
So raspeberries seem to have more vitamin and less water and Blackberries
'''
print(nutrition.loc[
    ['Raspberries, raw', 'Blackberries, raw'],
    ['protein', 'vitamin_b6', 'water']
])

'''
So that's extraction by label in the context of a data frame.
The big takeaway here is that we now have two dimensions to work with, which opens up new possibilities to interact with 
the data and these different techniques about selecting by size in policy in two dimensions, as well as the specific labels we want.
'''

