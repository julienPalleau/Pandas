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
When working with large datasets like ours, which has more than 8000 rows in 75 columns, it'll 
be really nice if we were able to quickly slice and dice the labels we're interested in.
And the good news is that to achieve that conveniently, we could use a method that we have talked about already.
The filter method. It's the same filter that we saw in the series section, but it's now got super powers because it allows
us to filter that index as well as a column and even both if we want.
Let's take a quick look at some concrete examples here. 
'''
print(nutrition.shape)
print(nutrition.head())
'''
Let's look at octopus entries.
nutrition.filter and I'll set the axis to zero because remember, I'm filtering in the index dimension,
in the nutrition data frame. That's where we have our food items. Their names for our food items.
So I want to filter in this dimension, and then I'll use the like parameter to say like octopus.
Looks like octopus has 41 milligrams of cholesterol.
'''
print()
print(nutrition.filter(like='Octopus', axis=0))

'''
Remember, using the like parameter here is similar to using a literal case, sensitive contains condition.
So if I drop this to lowercase or octopus. I get back to other matches, to other food items that belong to the same family
of foods, but were not initially selected because they were not capitalized.
'''
print()
print(nutrition.filter(like='octopus', axis=0))

'''
The good news is that this method also supports regular expressions, and this is a 
pretty good opportunity for us to use them.
A filter with regex. So far we used a filter with like.
We could say nutrition dot filter rejects octopus.
Ok with the line below we only got the lowercase octopus.
'''
print()
print(nutrition.filter(regex='octopus', axis=0))

'''
What do we do to get Octopus?
First, we could include a character class for the all.
Remember, the way we do that is just tuition, not filter rejects.
We would do character classes is within square brackets.
We specify a range or sequence of characters that we want to match.
And the order doesn't matter. But I'll say uppercase lowercase followed ctopus and by axis, is zero again.
So we're now matching all three.
'''
print()
print(nutrition.filter(regex='[Oo]ctopus', axis=0))

'''
We could, instead of using a character class to indicate that we want both uppercase and 
lowercase so we could ask regex to completely ignore case for this pattern.
In other words, match this patter in a case insensitive way.
And the way we specify that is by adding at the begining of our pattern, a question mark i within parenthesis.
Sure enough, we got all three occupier's matches in our data set, just like we did above.
Now don't worry if this look a bit weird right now, but using this i flag here we're simply saying that we want the pattern to match
without case being considered in regular expressions. In regular expression this is known as a modifier.
And in this particular case, the i is used for insensitive of case.
'''
print()
print(nutrition.filter(regex='(?i)octopus', axis=0))

'''
So far, we have filtered the data frame along the index. 
Remember, we keep specifying axis zero. 
But as you could probably imagine, by simply changing the axis argument here,
we could filter along the column dimension as well.
In fact, let's go ahead and do both at once. 
Filter along both dimensions, because thechnically I was only interested in knowing how much choldesterol octopus has.
I filter our column axis for cholesterol by chaining on a second filter method
specifying axis one of your column, and maybe to make this more readable I'll use a backslash forward to express
this command in two lines.
'''
print()
print(nutrition.filter(regex='(?i)octopus', axis=0).filter(regex='(?i)octopus', axis=1))

'''
So now, in addition to the like and regex parameters, the filter method also supports.
Another parameter called items, which allows us to specify the exact sequence of labels that we
want to match.
'''
print()
print(nutrition.filter(regex='(?i)octopus', axis=0).filter(items=['cholesterol', 'serving_size', 'calories'], axis=1))

'''
To be honest, I did it this way to demonstrate that the filter method can be 
used to filter along both the index and column axis. 
But for a use case like this, if we're targeting this DataFrame, as an end result, 
I would actually combine the filter method with the lock indexer
Like so instead of this second filter, methodology say lock and then I'll say select all
the rows returned from this first data frame.
In other words, only those that match these regex. And that on the column dimension.
'''
print()
print(nutrition.filter(regex='(?i)octopus', axis=0).loc[:, ['cholesterol', 'serving_size', 'calories']])