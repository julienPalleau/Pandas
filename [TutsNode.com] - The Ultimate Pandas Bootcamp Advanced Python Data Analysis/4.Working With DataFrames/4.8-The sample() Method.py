#W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
import pandas as pd
import requests

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',50)

'''
Let's introduce a nifty way which will use to conveniently take random smaples from our dataset. 
And that is the sample method, which is quite simple, actually.
We call it on a data frame and it returns back a random record or random observation.
The call it again, it should give us something else.
'''
url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")))
print(nutrition.sample())

'''
Let's print the column's name
'''
print()
print(f"Noms de toutes les colonnes:\n {nutrition.columns.values.tolist()}")

'''
Actually, there is a way to guarantee that these random method returns the same output for the both of us.
And that is if we provide the random state. So if we both said the MSA parameter to 12.
So normally random state is assigned in the background and it changes quickly thereby guaranteeing something
looks like randomness. But at the end of the day, it's not random. If we fix the random state parameter,
the behavior of this function is actually very deterministic and predictable, as we just saw here.
'''
#temporaly set expand_frame_repr
# with pd.option_context('expand_frame_repr', False):
#     print (nutrition.sample(random_state=12))
print(nutrition.sample(random_state=12))

'''
Simply specifies the number of recods that we want to get back that we're trying to sample. It defaults to one,
which is why we only saw one food item when we sampled without an argument both the step it up bit.
And you're getting I'm asking for three random observations.
So, for example, if we wanted to sample one percent of our data frame, we would pass 0.01
'''
print()
print(nutrition.sample(frac=.01))