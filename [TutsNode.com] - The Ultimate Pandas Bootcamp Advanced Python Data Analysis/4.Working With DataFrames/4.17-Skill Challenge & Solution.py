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
print(nutr_mini.loc[:, ['total_fat', 'cholesterol']])

'''
Exercice 3

Extract all the columns from bitamin_b12 to the end, for the first, second, and third rows.

Solution 3
'''