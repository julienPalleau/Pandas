# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

# Let's start talking about filtering,
# Let's say we want to only look at countries that start with v
print(alcohool.filter(regex='^V'))
print()
print(alcohool.filter(like='stan'))

# One thing to realise is that when we use filter (with regex or like) we filter along the key and not the value.
# What if we want to filter by value instead?
print(alcohool[alcohool > 200])
# or another way totally equivalent is:
print(alcohool.loc[alcohool > 200])


# we could as well create a little function to encapsulate the logic
def gt200(x):
    return x > 200


print(alcohool[gt200])

# The where() method: Replace values where the condition is False.
print(alcohool.where(lambda x: x > 200, other='too small'))

# If now we get ridooff other, too small is replaced by NaN
print(alcohool.where(lambda x: x > 200))

# Now if we simply chain the expression above with a dropna() method
print(alcohool.where(lambda x: x > 200).dropna())

# There is also the opposite of where method which again when combine with dropna() allow us to filter
# on account of condition being False.
# So above, with filter on a condition being True x > 200 but what if we want on a condition being false,
# 1st solution consists in flipping the criteria x > 200 in x < 200
print(alcohool.where(lambda x: x <= 200).dropna())

# But when it is not so simple to just flipping the comparator to get the opposit there is the mask() method
# So the line below match all the line where the condition is not true
print(alcohool.mask(lambda x: x > 200).dropna())
