# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling

import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

# # if we want to add 2 to our series:
# print(f"original values: {alcohool}, \noriginal value + 2: \n{alcohool + 2}")
#
# # if for whatever reason we want substract 10 and multiply the result by 2
# print((alcohol-10)*2)
#
# # As we have already mentioned one of the greatest feature of pandas datastructure is that the indexes align automatically
# # So let's see an example:
# print(alcohol.head())
# print()
# print(alcohol.sort_index(inplace=True))
print(alcohol.head())

more_drinks = pd.Series({'Albania': 6, 'Alberia': 19, 'Algeria': 10, 'Afghanistan': 100, 'Yemen': 101})

# Let's add alcohool with more_drinks using + operator
print()
print("Let's now add two series alcohol with + operator")
print(alcohool + more_drinks)

# Now let's try to add alcohool with more_drinks using add() function
print()
print('addition')
print("Let's now add two series alcohol with add() function")
print(alcohool.add(more_drinks, fill_value=0))

# Let's look at substract
# regular substract
print(alcohool - more_drinks)

# Pandas substract
print()
print('Substract')
print(alcohool.subtract(more_drinks, fill_value=0))

# The same goes for divide
print()
print('Divide')
print(alcohool.divide(more_drinks, fill_value=1))

# The same goes for multiplying
print()
print('Multiply')
print(alcohool.multiply(more_drinks, fill_value=1))

# The main advantage of Pandas operator is that the indexes don't need to be aligned, pandas will connect them by label before applying
# the applicable operator on the values
