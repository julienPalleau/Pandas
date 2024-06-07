# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
import pandas as pd
import requests

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',50)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col=0)
print(nutrition.head())
print()
print(nutrition.index)
print(type(nutrition.index))

'''
            RANGE VS INT64INDEX
    + RangeIndex is a special case of Int64Index
    + both are immutable, sequences of numbers
    + RangeIndex is an optimized alternative
'''
nutrition.index = pd.RangeIndex(start=0, stop=8789, step=1)
type(nutrition.index)

'''
What if we want to change is in that's from a series of integers, which is the case from both of this to something else.
Perhaps FullName. Let's get FullName. Well, to do that, we could rely on the SAT index method, which we have used
before, said indexed 'name'. Member name is the label of the column that we want to act as the index.
So we got a new data frame here that has a name as the index. Now, this is one of those methods that returns a copy.
So the underlying data frame is not modified. If we want to modify the data frame, what do we do? You guessed it.
We set in place to truth. 
'''
print()
print(nutrition.set_index('name'))

'''
So now if you look at nutrition and we see that the index has been changed to Name.
There's a couple of other parameter's that is set the index method subparts.
For example, one of the default is drop, which indicates whether the column being set as the new 
index should be removed from the resulting data frame. So right now, we're working with this.
Let's say wwe want to set a new index here, let's say.
So notice that folic acid disappeared from the columns that we had here.
And that is because the drop parameter defaults to true.
So these happen if we actually set this to false. Not only are we going to set folic acid as the index for this data frame, but we
will continue to have it as a column. 
'''
print()
print(nutrition.set_index('folic_acid'))

'''
Let's take a look. So now we see folic acid is the index, but it continues to live on as a column.
'''
print(nutrition.set_index('folic_acid', drop=False))

'''
There's also append, which gives us the option of appending a new index to the existing index.
It's works simply take some boolean. So if we say append true to the index.
Remember, this is our starting point, which is going to print it out here.
So we start with name in index. So now if we set folic acid, if we append folic acid to these existing index, we end up with what's
known in us as a multi index. So this is an index that has multiple levels. In this case, name and folic acid.
And lastly, there's verify integrity.
Verify integrity is a parameter that allows us to enforce the uniqueness of our index values.
So if we said verify integrity to true penthouse, we'll check whether the index contains unique values and we'll throw a value error if it doesn't.
If it contains duplicates, he will throw in a failure. Let's take a look.
Let's pick another column here, something that is bound to have non-unique values as your nutrition.
AP calories, calories, value counts.
'''
print()
print(nutrition.calories.value_counts())

'''
So the calories sequence of values contains 78 instances where the calorie count is exactly eight hundred and eighty four.
So let's try to set this as our index subsetting Daggs calories. And I'll set a very fine integrity to true.
So I'm asking pandas to confirm, at least you index that is being said has unique values.
So we know that will not be the case. And so we expect these to fail.
Appendices saying that the index has duplicate keys as we expected.
'''
print()
#print(nutrition.set_index('calories', verify_integrity=True))

'''
If we set this to false calories is set as the new index of our data frame.
'''
print(nutrition.set_index('calories', verify_integrity=False))

'''
Now, Pandas allows duplicates in the index, clearly. But I would strongly recommend against taking advantage of this feature.
More often than not, it will lead to poor peformance and confusing errors down the road.
This was the set index method, which we will use time and again to change the index of our data frame to any column we wish.
'''