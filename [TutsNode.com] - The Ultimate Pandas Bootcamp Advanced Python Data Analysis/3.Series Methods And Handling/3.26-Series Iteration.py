# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

mini_alc = alcohool[:10]
print(mini_alc)

# this iterates only on one column the value column.
print("default iteration: for i in mini_alc:")
for i in mini_alc:
    print(i)

# What if we wanted to iterate over the index label instead.
print()
print("Iteration over the index label")
for i in mini_alc.index:
    print(i)

# What if we wanted to get both index and values at once
for i in mini_alc.index:
    print(i, mini_alc[i])

#       Pandas also provide a much more convenient alternative that is the items method
print()
for i in mini_alc.items(): # this totally equivalent to mini_alc.iteritems()
    print(i)