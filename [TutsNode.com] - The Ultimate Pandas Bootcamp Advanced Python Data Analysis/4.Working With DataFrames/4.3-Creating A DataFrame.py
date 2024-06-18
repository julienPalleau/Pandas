# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames
import pandas as pd

# some python lists
names = ['Olga', 'Andrew', 'Brian', 'Telulah', 'Nicole', 'Tilda']
ages = [29, 21, 45, 23, 39, 46]
married = [False, True, True, True, False, True]

# To create a DataFrame from lists, you have to bear in mind that lists need to be equal length !!!
df = pd.DataFrame({'name': names, 'age': ages, 'married': married})
print(f"Data Frame created with 3 list with same length !!!\n {df}")
print()
print(f"longueur de names: {len(names)}")
new_names = names + ['Ryan']
print(f"longeur de new_names: {len(new_names)}")
# Let's try to rebuild a DataFrame avec new_names
# df2 = pd.DataFrame({'name': new_names, 'age': ages, 'married': married})
# print(df2)
print()

# The DataFrame constructor is also very flexible and support different concept inputs.
