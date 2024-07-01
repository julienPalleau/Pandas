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
In the previous lecture, before we dug into calculating the postassium to sodium ratio, we 
first looked at the foods with the highest postassium content.
And we did this in two steps.
It first started the series, and then we got the first 10 items using the head method.
So in other words, we chained two methods, sort values and had to produce this sinvle view here.
'''
print(nutrition.potassium.sort_values(ascending=False).head(10))

'''
But I think it's worth knowing that for this exact purpose of getting the largest X values and third
labels, we could also use a method that we have discussed before.
And that is the end largest method.
Because we're working with a data frame, though, we can simply say nutrition and largest 10, because
that's not enough information to determine what records to return.
Right, like Pandas doesn't have enough information in this case.
What column should Pandas be looking at to determine the largest?
To avoid that ambiguity, there is a second parameter called columns, this method, by the way, only
looks only works with this axis, which accepts a single column label or a list of column labels.
In this case, I'll just pass potassium ACMG.
And sure enough, we now get the same ten labels that we got above.
But we're now looking at a full data frame, a slice of them containing all the columns if we need output
from here.
We could further restrict this to only get what we want. 
In this case, I'll use the attribute accessor or don't access to just select potassium.
But before we execute that cell. Notice how similar these two are, right? In both cases.
We have the same 10 labels, but up above we have a series.
And down here, by using enlarges on the data frame, we get a full data frame containing the entire
column axis. So to restrict this further, I'll be indexing it.
Obviously, we can use log. ilog or square bracket here. Given the name is well formed,
I will use a access or attribute access here.
And sure enough, we now get two identical series back.
But this, looks a bit verbose and repetitive.
We're saying potassium twice here.
'''
print()
nutrition.replace('[a-zA-Z]', '', regex=True, inplace=True)
nutrition = nutrition.astype(float)
print(nutrition.nlargest(10, 'potassium', keep='last').potassium)

'''
And for this specific cas of looking at the top 10 foods by a single attribute, in this case, potassium,
I would prefer to first access that attribute and then use the enlargest method on the series instead
of DataFrame.
So, for example, we could say nutrition, not potassium, then use enlarges on that resulting series.
And obviously, when we use this approach, we don't have to specify a column because
we are applying the method to the series. And we know that series only have one sequence of labeled values.
So there's no ambiguity when we say enlarges. There's only one option at that point. 
But the two approaches clearly produce equivalent output.
Needless to say, the exact same mechanics apply that we discussed here with and largest apply with 
and smallest as well, which gives us the first and smallest records.
'''
print(nutrition.nsmallest(10, columns='potassium'))

'''
There are multiple options here, instead of passing a single label, we could also pass a list of labels.
So in this case, I'll say order by. To figure out the ten smallest observations, first order by sodium and then
order by calories and then by folate.
This multi-column sorting is something we can only do with DataFrame
'''
print(nutrition.nsmallest(10, ['sodium', 'calories', 'folate']))

'''
The biggest takeaway is that whenever we see a pattern of sorting values, followed by extracting a 
bunch of them, as we did here and in the previous lecture, we should always
think about using and smallest and largest instead, because these special purpose methods are a bit
more performant and chaining multiple methods, as we did here.
'''
