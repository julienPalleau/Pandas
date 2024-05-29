# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

'''
Exercice 1
Select all the countries from alcohol that have more than 50 wine servings, and save them (and the corresponding values) in a variable fifty_plus.
'''
print()
print("exercice 1")
fifty_plus = alcohol[alcohol > 50]
print(fifty_plus)

# Solution 1
# fifty_plus = alcohol[alcohol > 50]

'''
Exercice 2
From fifty_plus, choose the countries with the smallest 20 wine servings values.
'''
print()
print("exercice 2")
print(fifty_plus.nsmallest(20))

# Solution 2
# print(fifty_plus.nsmallest(20))

'''
Exercice 3
What is the mean, median and standard deviation for the sample from Step 2?
'''
print()
print("exercice 3")
print(f"quantile 50% is the same as : {fifty_plus.quantile(0.5)} median:{fifty_plus.median()}")
print()
print(fifty_plus.describe())

# Solution 3
# print(f"quantile 50%: {fifty_plus.quantile(0.5)}")
# print()
# print(fifty_plus.describe())
print()
print("Solution")
print(fifty_plus.nsmallest(n=20).median())
print(fifty_plus.nsmallest(n=20).mean())
print(fifty_plus.nsmallest(n=20).std())
