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
Let's start simple and extract. One of the food items we see here have again, I brought up the first couple of records here so that
we have them as reference and say we want to extract the fourth food item just like for series I look, indexing is zero based for data frames, too.
So to extract the four item, we say the fourth item was a nutrition iloc like three.
'''
print()
print(f'nutrition.iloc[3]')
print(nutrition.iloc[3])

'''
So now we have staff here and these returns, again append us series that, by the way, is we could have also gotten by saying, I like Colin.
Where three indicates that we want the fourth observation and colon indicates that we want all the columns for that fourth Earl.
'''
print()
print(f'nutrition.iloc[3, :]')
print(nutrition.iloc[3, :])

'''
Ok, now go for Rows, four, six and nince say Saltaire and nutrition iloc.
Remember, the first argument specifies the rows and the second columns.
But because we're interested in non-contiguous records, in other words, those that are not consecutive.
We have to pass a list of integers, say, four, six and nince.
So I'm passing a list of three integers and then in a second parameter, I'll just pass a column to select all.
'''
print()
print('nutrition.iloc[[4, 6, 9], :]')
print(nutrition.iloc[[4, 6, 9], :])

'''
And again, this is equivalent to just not specifying the second parameter as well.
Even if we drop it, it still give us all the columns.
'''
print()
print(nutrition.iloc[[4, 6, 9]])

'''
Now, instead of all columns, maybe we're interested in only looking at one of them. Say for example total fat.
We want to figure out the local set for these three food items. 
We could do that by replacing the colon with something more specific. 
And this is where we have to be careful because I look supports extraction by position.
We can simply say total fat here: nutrition.iloc[[4, 6, 9], 'total_fat'].
We can use a label to do our selection.
Instead of seeing total fat, the label realizing that total fat is the third column or, in other
words, position two in our data frame. We simply say 2 here:
And we got the total fat content for these three records that we've specified that we've selected.
'''
print()
print(nutrition.iloc[[4, 6, 9], 2])

'''
And what if we wanted total fat, staturated fat and cholesterol?
Instead of 2, which selects total fat, we can use a slice taking advantage of the fact that these
three columns that we're now interested in are consecutive. So we say go from two to five exposure.
Sure enough, we now get a data frame containing selecting these three nonconsecutive in rows, as well
as these three consecutive our columns.
'''
print()
print(nutrition.iloc[[4, 6, 9], 2:5])

'''
Another thing worth mentioning is that both the Iloc and Lock indexers support boolean mask of data, frames too.
And the syntax is identical to what we saw for series, except it now extends over both axes.
'''
# boolean masks
'''
Remember that when we use boolean masks for series, we had to provide a list of booleans sequence of booleans.
That was exactly equal to the length of the series. Now that we are working with data frames, we have to provide till sample is
one that is exactly matching in length to the row axis and the other that has the same length as the column axis.
For example, in order to access every other column and every other row, we could say something like
'''
print()
new_nutr = nutrition.iloc[
    [True if i%2==0 else False for i in range(8789)], # raw length
    [True if i%2==0 else False for i in range(76)] # column length
]
print(new_nutr)

'''
So with code above we get a new DataFrame that has about one fourth the observation of our main DataFrame.
The reason for that one fourth is that both dimensions are being carved.
So if before we had to take a look here, let me sign this to a new variable, new nutrition. 
so if before we had nutrition and shape, X rows and Y columns, we now have new nutrition and odd shape.
We now have about X over two columns, right, X over two rows and Y over two columns, which means
that if the number of observations was X times Y, in this case, the number of observations now is X 
times Y over four.
So we apparently have about one fourth, the observations if we do these kind of boolean masking here.
'''
print(nutrition.shape) # x rows and y columns
print(new_nutr.shape)

'''
In this lecture, we've seen a lot of slicing and extraction of many elements at once.
But what if we're interested in something very basic in only one specific value?
'''
print(nutrition.head())

'''
What if we say we're interested in only figuring out the calories for vegetarian filets?
All we have to do in this case is identify the coordinate for that value.
Exactly wehre is this value located in this plane?
And in this case, that the ninth index. And the first column position, so zero and then zero all the way up to nine.
This works great, but for single value extraction, however, Pandas has some dedicated attributes, 
which are a lot more performant or quicker and will cover these in the next lecture.
And I would definiely recommend using those for a single value extraction.
'''
print(nutrition.iloc[9,1])