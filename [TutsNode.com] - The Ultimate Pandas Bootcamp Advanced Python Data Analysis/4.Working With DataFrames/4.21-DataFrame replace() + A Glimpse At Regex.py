# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
import pandas as pd
import requests
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 50)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col='name')  # we position the index column on name column

'''
In the previous lecture, we saw that the astype() method would not really PR one stop solution for 
converting the nutrition data frame to a purely numeric data frame. 
We came to the conclusion that we would first have to separate the units from the values and then apply
as type to the values. For that, we are going to use the replace method. And this is a very intuitive.
It does exactly waht the name implies. It replaces one thing with another.
As always, let's first look a this method in isolation, but start by applying it to a chunk of our nutrition data frame.
And for this one, I will select the first six rows and maybe choose the first column. Serving size.
Notice that serving size is a column of Dtype object right now. It contains only strings.
And that makes sense, right? Because of this G here, the units.
'''
print(nutrition.iloc[:6, :2])

'''
So if you look at info, we see that it is an object dtype.
'''
print()
print(nutrition.iloc[:6, :2].info())

dfm = nutrition.iloc[:6, :2]
'''
The way the replace method works is we pass an argument to the replace parameter to indicate what we want to replace.
Let me get the mean scientist to a variable first.
So call it dfm and then we'll call the replace method on the form.
There's a bit of an issue with what we're doing here.
'''
print()
print("---")
dfm.infer_objects(copy=False)
pd.set_option('future.no_silent_downcasting', True)
print(dfm.replace(to_replace='100 g', value=100, regex=True))

'''
The way we've used replace so far is very nitpicky as it depends on extact strings matching.
We're saying 100 g, needs to be repalced with 100.
Ideally, we'd like to only replace the units.
'''

'''
There is a more flexible way we have to deal with string replacement using this method, using the replace method, and it involves projects.
It involve the regex. 
A good web site to test your regex is regex101
'''
print(dfm.replace(r'\sg', '', regex=True).astype(int).info())

''''
But are we ready to scale this up to the entire data frame?
I'll say nutrition that had to break up the first 10 records or so.
This method we have above is replacement strategy we have here will not work for all the columns.
Because so far, we've defined only one pattern space followed by G. But notice that some columns
Do not have a space. And other columns are not defined in grams, but milligrams or Milli centigrams.
'''
print(nutrition.head(10))

'''
For those cases our pattern would fail. 
So it looks like we'll have to specify more patterns to cover the outer units.
But there are better ways when se started playing with tax, we will see several other ways to handle similar situations.
One approach is to simply use rejects to replace away any part of the string that is not numeric that 
are included that would capture all of these units.
Because we're saying take everything that is not numerice and remove it from the string.
But for us that approach is not the best in our context, because maybe it's not a good idea to completely get rid of our units after all.
I think in the past, in fact, if we merge then into our column names.
So we say serving size, underscore G total fat, underscore G sodium, underscore MG and so on.
I think that's a better approach.
That way, we're not loosing information, we're regrouping it in a mannner that makes more sens for our analysis.
'''