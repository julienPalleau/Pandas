#W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
import pandas as pd
import requests

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',50)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col=0)
print(nutrition.sample(n=3, replace=True))

print(nutrition.sample())
'''
We said that the sample method in Pandas chooses a random observation for our population.
We've been seeing variations of nutrition sample throughout last couple of lectures.
The question now is how does pandas actually decide this?
How does pandas get random and decide to give us the observation with the index label six two, two nine
The answer to this question goes beyond pandas in Python and more into computer science in general.
You see, when we observe random phenomena in the world like radio noise or cosmic background radiation, 
we're witnessing what physicists call natural entropy. Think of this as true randommess.
And in simple term that means that what we observe now tells us nothing about what comes next.
And you could keep observing the same process and the same output.
And we won't be able to get my predictiveness out of it.
We won't be getting better at predicting what comes next.
So this is what we mean by true randomness.
It's actually very hard to source these natural entropy due to measurement biases and rate limits.
But there are many creatives ways that scientists go about this.
There is a web site in charge of generating random number random.org
'''
