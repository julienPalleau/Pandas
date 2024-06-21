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
We've talked about data frame extraction by position or label across the index and column dimensions,
but especially when working with numerical data frames, there are a couple of other really powerful
approaches that combine series methods with data frame extraction capabilities.
One of them is the series between methods, which gives us a convenient way to specify a range values
to select based on a range of values. Now, this is a series method, so we can just go ahead and apply to the entire
DataFrame. So first, we have to select a one-dimensional slice from our data frame there for a series.
And it could be a row or a column, but it needs to be one dimensional so that we get back a series in this case,
I'll use a column, remember the shape of our DataFrame. We have to select a given dimension here that is had represents a series.
I'll go with a column because it makes a lot more sense for the data we're working with.
And specifically, I'll go with calories. Take a look at the first couple of records.
'''
print(nutrition.calories.head(10))

'''
So here we have a pen series containing the calories across all foods. No big surprises here.
Now let's extract some label values from the series using the between method.
Say we are looking for a healthy, low calorie snack.
And our definition of that is something that contains between 20 and 50 calories for 100 grams serving
remember all nutrition information in our data frame, you standardize to 100 grams.
So to figure out what those four items are, we can simply say calories, God, between 20 and 60.
These are both inclusive, by the way.
'''
print()
print(nutrition.calories.between(20, 60))
'''
So includes 20 and 60 as well as any number within that range.
So when we get back is a billions series that has the same length as our original data frame index or 
has this series. So if we check the length for this, maybe it'll just go with shape.
'''
print()
print(nutrition.calories.shape)
print(nutrition.shape)

'''
It's exactly the same as the original length.
For example, for the series that we applied between two.
Which also equal to the length of the index of our main data frame.
All these are the same length. But this one is a boolean mask.
So it includes all of those labels associated with true and false values.
Wherever are caloric contact, the calories value falls between 20 and 60 is
marked with the true.
'''
print()
print(nutrition.calories.between(20, 60))
'''
And wherever it falls outside that range, either on the low end or higher, and it is marked with falese.
Now let's use this bullying mask to extract from our original data frame.
As we've done before, we simply take this panda series of booleans and we pass it to square brackets
on the main DataFrame. So we're seeing nutrition, square brackets, nutrition, gold calories between 20 and 60.
It's look like, we'll get almost a thousand back, more than a thousand. 
'''
print()
print(nutrition[nutrition.calories.between(20, 60)])

'''
OK, but maybe a thousand items is probably overwhelming.
Maybe we're only looking for a couple of suggestions.
So let's combine this result with sample and get four back.
Let's get a random sample of four item back.
'''
print()
print(nutrition[nutrition.calories.between(20, 60)].sample(4))

'''
Remember, behind the scenes, all that's really happening is that a series of booleans is first created
by this between method here.
And then it is used to extract values from our DataFrame, using boolean indexing with square bracket, 
which we've explored before. So now think that we're not familiar with.
But notice how expressive this syntax is. 
We're saying select from nutrition, where calories are between 20 and 60.
And give me a random four out of that, a random four results out of everything that is returned.
It almost reads like English.
'''