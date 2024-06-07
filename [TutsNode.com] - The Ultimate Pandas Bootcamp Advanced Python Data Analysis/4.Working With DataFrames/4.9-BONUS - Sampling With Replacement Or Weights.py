#W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
import pandas as pd
import requests

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',50)

'''
The simple method could get fancier that what we described in the previous lecture.
And I wanted to quickly go over two key parameters here, because I think they will be useful if you 
continue on to do statistical work or analysis. The first is simply with replacement. 
And what this basically means is that whenever we sample records from our population, we place that
records so that the probability of picking the same item again remains unchanged.
Think of sampling as choosing something from a hat. And the hat contains all that possible values in a population when we sample
with replacement. We choose to put this record, this thing that we just select it back into the hat.
Another way to says this is that sampling with replacement makes it possible to pick the exact same record multiple times.
This is also known as bootstrapping in statistics. 
So let's see how we can do with or without replacement sampling, with or without replacement.
'''

'''
Let's introduce a nifty way which will use to conveniently take random smaples from our dataset. 
And that is the sample method, which is quite simple, actually.
We call it on a data frame and it returns back a random record or random observation.
The call it again, it should give us something else.
'''
url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col=0)
print(nutrition.sample(n=3, replace=True))

'''
The next parameter we'll talk about allow us to break the randomness assumption this sampling process.
'''

# weighted sampling
'''
If you think about what random sampling means, it's simply saying that the probability of choosing 
any one sample or element from the set is equal. 
With weights, we break that because we lable our samples with specific weights and then we take those 
weights into consideration when we do the sampling. The higher the weight of, the more likely the sample will be chosen.
May be an example is easier. There's many ways to use the weights parameter.
But here I'll simply create a Pandas series. And I'll sign on the weights variable. weights = pd.Series
And then to the data parameter, I'll pass. I'll specify the weights and think of these as relative weights, because Pandas
will normalize them behind the scene anyway. In other words, these don't necessarily have to add up to one or 100 percent or
anything like that. So these are my weights. So I want three values to be very likely to be selected. These are the heavy weights.
And then the next one to have a much lower probability of being selected. And then the last we have a higher but still relativvely small
probability of being picked. Next to the index parameter, I will pass the values that I'm interested in sampling by referencing
their index labels. So these are the ones I look I want to very heavily wait. In other words, make likely to be picked.
And then for the low lowest probability, one, I'll say five and six for more likely, but still unlikely.
So this is our weights
'''
weights = pd.Series(data=[10, 10, 10, 1, 2], index=[7, 17, 29, 5, 6])
print(weights)

'''
So then we can go ahead and use the weights in our sample.
'''
print()
print(nutrition.sample(n=3, weights=weights))

'''
So think of weights as a way of expressing our preference for what we want ot be sampled.
We started our sampling by picking five and then six, which I guess is very relatively unlikely because
our last four samples have been exclusively seven, 17 and 29 are heavily weighted indices here.
Now, this may not be very useful beyond the scenario of peaking seven, 17 and 29 with a higher likelihood.
But imagine what we could do with this kind of functionality. 
For instance, if the index were another more meaningful field, we could sample using diffent weights
depending on the contents of the index.
In any case, I only wanted to point out that sampling in pandas does not have to be random equal weight.
We could allow or prevent replacements and even provide specific weights to bias the sampling one way or another.
'''