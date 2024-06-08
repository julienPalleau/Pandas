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

'''
In the previous two lectures, we saw the power and flexibility of extracting by label and position using those loc and iloc indexers.
In the end, we also demonstrated how to extract single values using these two indexing attributes for
a quick recap with label based extraction. To access a single value, we only need to specify the respective index and
column labels so we can sy loc nuts, pecans and then calories. 
And with position based indexing would do the same, but with positions instead.
We're back to calories for pecans again for single value extraction however, pandas does 
offer two highly efficient alternatives. 
'''
print()
print(nutrition.loc['Nuts, pecans', 'calories'])

'''
The at and iat attributes which just like the loc and iloc attributes our
indexing attributes to, for example, if we're interested in extracting a single value by label, we could say nutrition, at
'''
print()
print(nutrition.at['Nuts, pecans', 'calories'])

'''
So at is kind of the equivalent of luck, i.e label based extraction, but only for single value access.
And if similarly, we want to do the same by position we used to, I had attributed to nutrition.
'''
print()
print(nutrition.iat[1, 2])

'''
But why would we ever consider using at an iat when log and ilog this exact syntax and functionality?

                        Why use .at or .iat?
    SINGLE-PURPOSE unlike .loc or .iloc, .at and .iat are only used for accessing single value
    
    FASTER because of the lack of overhead, they are much more performant for their isolated use-case
    
Think of at and iat as highly specialized.
They have a single purpose, and that is to extract or select a single value from a pandas data frame,
because they only do this, one thing. They manage to do it really quickly.
So lok, and iloc on the other hand, have some overhead, because they first have to determine what syntax applies.
They have to figure out whether we, the users, are trying to index using booleans slices or maybe 
single indices because of this flexibility and syntax that they offer.
Their performance is slower than it is for at and iat, which because they're more specialized, they
do their job a lot quicker. Let's try to put some numbers to all of this.
I'll do a comparison here to do the comparison will use a line magic from python to time, many, many
executions of loc base extraction and then compared those to extracting with the at indexer from this lecture.
So I'll take time it, I'll say nutrition dot loc.
'''

'''
For example, it chose to run 100000 loops based on its assesment of how quickly these function runs.
We see it took about 0.71 seconds.
'''
import timeit

print(f'using loc: {timeit.timeit('nutrition.loc["Nuts, pecans", "calories"]', globals=globals(), number=100000)}')

'''
Let's run the at indexing extraction for comparison
So we can see that .at take roughly half the time compare to .loc solution. 
'''
print(f'using at: {timeit.timeit('nutrition.at["Nuts, pecans", "calories"]', globals=globals(), number=100000)}')

'''
When you start working with massive data sets and more complicate alogorithms, this difference could add up to something substantial.
So it's really good to be aware. When using/needing single value access, please prefer at and iat over loc and iloc
'''