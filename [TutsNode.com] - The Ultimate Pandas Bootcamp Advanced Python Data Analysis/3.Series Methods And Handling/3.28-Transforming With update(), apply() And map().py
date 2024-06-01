# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd
import numpy as np

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

# Let's talk about some really important really usefull functions that help us to transform our series
# When it comes to transformation in pandas we could really think of two broad categories:
#   1 - There are those that target a couple of specific records
#           saying modifying the value of Algeria, Albania
print(f"Algeria: {alcohool.loc['Algeria']}")

# spot vs global transform
alcohool.loc['Algeria'] = 19  # we use the equal assignment

# We can see that algeria has been updated to 19
print(f"Algeria after we updated the value with alcohool.loc['Algeria']=19: {alcohool.loc['Algeria']}")

# Let's update as well Albania, Afghanistan, Andorra
alcohool.loc['Albania'] = 190
alcohool.loc['Afghanistan'] = 20
alcohool.loc['Andorra'] = 29

print(alcohool.head(10))

# The only problem with the approach above is that it doesn't scale very well.
# For such instances, it might be useful to consider the hande update method which modify the series in place using non na values
# update always operate in place.
alcohool.update(pd.Series(data=[200, 20, 20, 29], index=['Albania', 'Afghanistan', 'Algeria', 'Andorra']))
print(alcohool.head(10))

# What if we intend to apply a common transformation to all the elements in our series?

# 1st solution (prefered one) - Apply() methode is the most flexible
print(alcohool.apply(lambda x: x ** 2))

# 2nd solution
print(alcohool.apply(np.square))


# 3rd solution
def multiply_by_self(x):
    return x * x


print(alcohool.apply(multiply_by_self))

# So we have 3 different equivalent approaches to squaring the number of wine serving
# BTW we could also pass additional arguments or keyword arguments to our function to make them behave in more custom ways.

# Let's say that instead of squaring all the values we only want to square the ones below a minimal amount.
print()


def multiply_by_self_with_min(x, min_servings):
    if x < min_servings:
        return x ** 2
    return x


# How the line below works? x is reserved for the series, the next positional argument is 200
# One approach is to use multi parameter function like below, in using positional arguments like we did here in our args tuple.
print(alcohool.apply(multiply_by_self_with_min, args=(200, )))

print(alcohool.head())

# The other approach is to use keyword arguments a key arg that match is our parameter name
print(alcohool.apply(multiply_by_self_with_min, min_servings=200))

# Another approach to applying global transformation is to use the map() method
# the map() method. But be carreful map() doesn't work with more complex transformation, for example, callables that accept parameters
# map and apply are no longer substitute.
print(alcohool.map(lambda x: x**2))

'''
                Transforms

update(): modifies series values in place using another series
    ser.update(other_series)
    
apply(): applies function (or ufunc) on each serie value
    ser.apply(np.sqrt)
    
map(): subs series values with others from a function, series, or dict
    ser.map({old_value':'new_value'})
'''
