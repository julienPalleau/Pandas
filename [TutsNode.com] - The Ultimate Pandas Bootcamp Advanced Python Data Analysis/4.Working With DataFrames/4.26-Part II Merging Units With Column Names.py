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
units = nutrition.astype(str).replace('[^a-zA-Z]', '', regex=True)

'''
            Our Data Prep Process
    ----------------------------------------------------------------------------------------->
    COLLECT                 CREATE                          RENAME
    UNITS                   MAPPER                          DF
    isolate the units       create a dictionary of          replace all the units
    from each nutrition     key:value pairs                 from the dataframe
    column label            containing the old              values and convert
                            labels and the new              values to floats
                            
Our goal in this lecture would be to take the units we isolated a couple of lectures ago and merge them
into the column labels so that we don't completely discard that information.
Remember, a bigger purpose here is to get to nutrition data frame that is all numeric.
But at the same time, we don't want to lose information on what their album units are because they're
different across each nutrition column label here, and they carry some information.
For instance, if we see 6.2 under saturated fat and then 600 under vitamin D.
We could not really compare the two numbers becase the fat is in grams, whereas vitamin D in international units.
Sixteen hundred of which is probably like a few micrograms.
The point is, yes, we would prefer a numerical dataset instead of these strings that we have here.
But at the same time, we don't want to lose track of the units because we feel that they are relevant to the interpretation of our data.
So restarting this lecture with a data frame that contains the units and only the units. 
Remember, we prepared this some lectures ago and we called it simply units.
So at this point, we are ready to merge these into the column names up here.
To do that will rely on the rename method, which we introduced in a previous lecture, as we saw at 
that method, expects a map of the old lables and the new ones. So let's create that map.
Do use a dictionary comprehension to delete their rename method PR solution, and I'll use a dictionary
comprehension later in the lecture to appeal at the perhaps before we get to that.
We should briefly familiarize ourselves with how to iterate over these units data frame.
'''
# print(nutrition.head)
# print(units.head)

'''
A data frame, iteration, determ data frame iteration in a nutshell.
So if we wanted to get a trade overeagerness, we can start with a basic python.
I'll say four K in units, let's just print it out to begin with.
'''
# for k in units:
#     print(k)

'''
We are also interested in the units associated with each column.
I also use square brackets to access the unit associated with the label.
So now we have where we're all putting a long sequence of column labels, as well as the associated labels.
'''
# for k in units:
#     print(k, units[k].iat[0])

'''
Notice there's a couple of gaps like calories is in have a gap.
It'd be easier if I just remove the column name entirely and we only print the units.
So these gaps are now very obvious. 
So this is for nutritional factors they do not have a unit in our dataset.
May be we should simply exclude this entirely.
'''
# for k in units:
#     print(units[k].iat[0])

'''
I'm going to do that in two steps, possibly in one line.
I'll first replace all the anti values, these gaps using the replace method.
So I'd say replace anti with nan and then I'll drop nan drop all the columns that contain nan.
So what remains is technically only the columns that contain a unit and then all the scientists to the 
U.N is variable.
'''

# #print(units)
units.infer_objects(copy=False)
pd.set_option('future.no_silent_downcasting', True)
# units = units.replace('', np.nan).dropna(axis=1)
print(units.head())

'''
So if we now iterate over units and we print the units there are remaining use at, we say that there's no gap anymore.
'''

# for k in units:
#     print(units[k].iat[0])

'''
So we now have some clarity on how to iterate over the units data frame to get precisely what we want.
The column labels and the corresponding units.
What we did here is a tradiotional python look, which I only use to demonstrate the iteration dynamics
that will apply behind the scene when we build our mapper object using a dictionary comprehension.
'''

'''
So in the previous lecture, we collected all the units remembering that units data frame.
And now we about to create a map here, which is going to be a dictionary of key value pairs containing
the old tables and the new labels.
Remember, the new labels will append that unit to the common name. 
And the reason we create this paper is because we want to pass it to the rename method, which we will
call on the nutritional nutrition data frame. In order to do the remaining.
So by the end of this lecture we will have completed the first three steps in our data preparation process here.
And then in the next one will wrap up this last step.
So essentially we're going to create an object that look like with say serving size.
Remember this is a long sequence of key values.
The key will contain the old common label and the value will contain the new current level, which will be serving_size_g
and similarly total_fat_g and so on.
So this is our target object.
'''
# {
#     'serving_size': 'serving_size_g',
#     'total_fat': 'totat_fat_g',
#     ...
# }


'''
Let's use a dictionary comprehension to put this object together in a very pythonesque way.
I'll assign to the mapper variable.
'''
# print()
# mapper = {k:units[k].iat[0] for k in units}
# print(mapper)

'''
But notice that we don't want to replace the all column labels with just the units.
We want the units to be embedded into the column names, not to replace them entirely.
So let's make a quick change up here to concatenate the existing column names with the unit.
Instead of just units, I'll say key plus underscore plus units.
'''
print()
mapper = {k:k+'_'+units[k].iat[0] for k in units}
print(mapper)