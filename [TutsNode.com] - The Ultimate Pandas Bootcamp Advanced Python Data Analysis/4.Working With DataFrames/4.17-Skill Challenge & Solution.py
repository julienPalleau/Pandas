# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames


'''
Exercice 1
Randomly select 10 food items assign the resulting dataframe to a new variable called nutr_mini
'''
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
Solution 1

The reason why simple works this way. Why it gives us 10 rows instead of 10 columns?
Is because there is a silent parameter here and access that is defaulting to none are zero.
And that means that we want to sample from that index axis.
So we want to select a ranodm rows as opposed to ranom columns.
So that's why we get this.
If we flip this to one now, we're indicating to us that, yes, we want 10 random records.
We want our sampling to happen along the column axis. We want 10 random columns.
So if you take a look at sampling without access, now we see that we got all the rows and 10 columns.
'''
print()
print('Exercice 1')
nutr_mini = nutrition.sample(10, axis=0)
print(nutr_mini.shape)

# nutr_mini = nutrition.sample(10, axis=1) # if uncomented the next exercise won't work.
# print(nutr_mini.shape)
print(nutr_mini.info(memory_usage='deep'))

'''
Exercice 2

From nutr_mini, extract the total_fat and cholesterol columns for all rows.

Solution 2

Remember, the typical way to extract using labels are passing a column to indicate, I want all 
the rows and then I'll pass in a python list of labels to indicate exactly columns.
Why are we passing a python a python list instead of a slice? 
Well, it's because these columns, happend to be non-contiguous. Like they're not next to each other.
Total_fat is here and then we have to skip saturated fat and go for cholesterol.
So the way to do that is to specify that we want this and that. Forget about the rest
We now have a new data frame that contains all the rows from our smaller data frame here.
And there's only 10 of them because we sampled up here and then only two of the columns.
'''
print()
print('Exercice 2')
print(nutr_mini.loc[:, ['total_fat', 'cholesterol']])

'''
Exercice 3

Extract all the columns from bitamin_b12 to the end, for the first, second, and third rows.

Solution 3

We're asked to extract all the columns from vitamin B to the very end for the first, second and third rows.
We have a bit of a problem here, because on the columns front, we're talking about a label base slice.
So we're saying start with vitamin B12 column label and go to the very end.
But they're not on the roll front on the index side of things. We're talking about poistions.
We're seeing first, second and third rows. So we have a couple of options here 
We can either convert this to a position and then work with integer locations for both columns and index
labels that I'm sorry, index axis, or we can convert these first, second and third to labels and
then work with labels on both sides. 
But because this is a single value, I much rather convert these to a location and then rely on a location
based extraction approach. So I'm going to go with that. 
But I think it's worth knowing that there's many more ways to go about this.
We called it not immediate. 
'''
print()
print('Exercice 3')
print(nutr_mini.iloc[0:2, :])
# or
'''
So I want ot figure out where vitamin B12 is sitting on that axis.
And I get back position 21, which means that it's the twenty second column in our data frame.
'''
b12_loc = nutr_mini.columns.get_loc('vitamin_b12')
print(f"I get back position: {nutr_mini.columns.get_loc('vitamin_b12')}st")
'''
And now we are ready to use an integer, location based extraction approach.
So we want to first through third. 
So I'm going to say zero to three member position.
This is exclusive.
And then I'll say be 12th lock all the way to the very end.
So like column with without a specified end.
We get a new data frame that has the first three items selected from our data fame,
as well as all the columns from vitamin B12 to the very end
Now, one thing to notice here, obviously, is that in all of these results, because were 
starting with our random ten.  Obviously, my results will be different from your most likely.
'''
print(nutr_mini.iloc[0:3, b12_loc:])

'''
Get the calories for the third food in nutr_mini using an attribute-based approach that is faster than .loc or .iloc.
'''
print()
print('Exercice 4')
'''
Exercice 4

Get the calories for the third food in nutr_mini using an attribute-based approach that is faster than .loc or .iloc

Solution 4
We're asked to get the calories for the third foot in our nutrition mini DataFrame using an attribute based approach that is faster than our ilog.
So what would those be? Those are the single value access attribute indexers that we talked about.
So specifically at and iat.
So let's take a look here so far. 
So we simply need to say iat two one.
'''
print(nutr_mini.head())
print(nutr_mini.iat[3, 2])
