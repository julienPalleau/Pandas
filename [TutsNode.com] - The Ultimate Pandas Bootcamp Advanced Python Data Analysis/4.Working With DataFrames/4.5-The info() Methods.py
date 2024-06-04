# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames
import pandas as pd
# some python lists
names = ['Olga', 'Andrew', 'Brian', 'Telulah', 'Nicole', 'Tilda']
ages = [29, 21, 45, 23, 39, 46]
married = [False, True, True, True, False, True]
df = pd.DataFrame({'names': names, 'ages': ages, 'married': married})

# One of the first things to do when preparing to work with the new dataframe is to look at a brief summary of what it consists of.
# For it contains and the infamous. It gets us exactly that in a nushell.
# So we say DataFrame info and we get this nice little output here.
# Notice, this method only works for DataFrames.
# So the class at top here that says data frame, it's not surprising.
# And next, we have a description of the index. In this case, the familiar Pandas Range Index object going from zero to five
# and coming the data columns where we get the name of the column number of non-null values it contains, as well
# as the respective data attached at the very end. We are shown a data frame level summary of the types and an estimate of how
# much space in memory our data frame takes this memory usage.
# Now our data frame is pretty small, as it only contains three columns.
# But if we add a much bigger dataset with many columns, this output would get a bit overwhelming as it would extend
# and DOWNBELOW to deal with that. We have two parameters in the info method, which we could specify.
print()
print(f"we get info on data frame with df.info(): {df.info()}")

# Let's start with verbose. So we can say setting verbose to false will ensure that no info on the specific
# columns is printed.
print("---")
print(f"we get less info on data frame with df.info(verbose=False): {df.info(verbose=False)}")

# Alternatively, though, we could specify the max calls parameter to give us an indication of the upper-bound
# number of columns after which it should switch to the truncated output.
# So let's start with Farior. If we call max calls with four, we get everything because our data frame only has three,
# So this upper bound of four has not been reached yet.
# But if we switch down to two, the cons, the specifics are trucated there.
print("---")
print(f"If we pass max_cols=2 we get only two: {df.info(max_cols=2)}")

# I think the most interesting parameter in this method is the memory usage parameter. And this parameter also takes booleans.
# The True and False cases are relatively straightforward. So False doesn't give a memory usage at all
print(f"If we pass memory_usage False we don't get anymore info about memory usage: {df.info(memory_usage=False)}")
# And setting it True gives us the estimate.
print(f"If we pass memory_usage True we get an estimate: {df.info(memory_usage=True)}")

# But where it gets interesting is with a deep argument, because the memory usage we see here.
# Is an estimate based on the datatype Sanader words, Pandas estimates.
print(f"If we pass memory_usage deep is also an estimate: {df.info(memory_usage='deep')}")