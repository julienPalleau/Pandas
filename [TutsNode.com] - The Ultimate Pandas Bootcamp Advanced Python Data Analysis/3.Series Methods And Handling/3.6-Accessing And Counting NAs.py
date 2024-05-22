# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohol = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohol = alcohol.squeeze('columns')
# print(alcohol.isnull())
print(alcohol[alcohol.isnull()])

print()
print(alcohol[alcohol.isnull()].index)

# Lets look at type of alcohool[alcohol.isnul()]
print()
print(type(alcohol[alcohol.isnull()].index))

# We get back the index under a list form.
print()
print(list(alcohol[alcohol.isnull()].index))

# Let's shift our attention to counting (counting nulls)
print()
print(len(list(alcohol[alcohol.isnull()].index)))
# cumbersome: very difficult to work with. The expression above to count the number of null entry is cumbersome
# antonyms: pandorable => adorable and involving pandas
print(alcohol.isnull().sum())
# booleans are integers in python
print()
print(sum([True, False, True]))

# Let's confirm we have our serie fully accounted for in terms of the count of values by type:
all = alcohol.size
nonnulls = alcohol.count()
nulls = alcohol.isnull().sum()
print(f"all: {all}, nonulls: {nonnulls}, nulls: {nulls}, all==nonnulls + nulls: {all == nonnulls + nulls}")

print()
'''
!!!IMPORTANT!!!
Each time we have used isnull() we could have used isna()!
'''
print("""!!!IMPORTANT!!!
Each time we have used isnull() we could have used isna()!""")
na = alcohol.isna().sum()
print(f"all: {all}, nonulls: {nonnulls}, na: {na}, all==nonnulls + na: {all == nonnulls + na}")

'''
            Series Accounting
+ .size: number of elements in the series
    series.size # 193
+ .count(): number of non-null elements
    series.count() # 162
+ .isna().sum(): number of null elements
    series.isna().sum() # 31
'''