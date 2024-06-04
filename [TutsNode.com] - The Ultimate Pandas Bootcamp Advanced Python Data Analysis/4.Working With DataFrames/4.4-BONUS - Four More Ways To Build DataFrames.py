# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames
import pandas as pd

'''
        MORE WAYS TO DATAFRAME
        
    + dict of tuples                                        + dict of dicts
    like dict of lists, but with tuples                     key: value pairs with column names as
                                                            keys and index-labeled key:value pairs
    column-wise                                             containing values
                                                            
                                                            column-wise
    

    + dict of series                                        + list of dicts
    a continuation of key concept #2                        list of key:value pairs containing column
                                                            labels and values
    column-wise                                                        
                                                            row-wise
'''
# some python lists
names = ['Olga', 'Andrew', 'Brian', 'Telulah', 'Nicole', 'Tilda']
ages = [29, 21, 45, 23, 39, 46]
married = [False, True, True, True, False, True]

# we convert our 3 lists in tupples to create a DataFrame with + dict of tuples
tuple_names = tuple(names)
tuple_ages = tuple(ages)
tuple_married = tuple(married)
print(f'tuple_names: {tuple_names}')
print(f'tuple_ages: {tuple_ages}')
print(f'tuple_married: {tuple_married}')
# So now we have 3 tuples, both list and tuples are ordered and iterable but unlike list tuples are imutable
print()
print(f'tuple_names: {tuple_names}')
print(f'list: {names}')

# 1 - dict of tuples
print()
print('1 - dict of tuples')
df = pd.DataFrame({'name': tuple_names, 'ages': tuple_ages, 'married': tuple_married})
print(df)

'''
        MORE WAYS TO DATAFRAME
        
    + dict of tuples                            + dict of dicts
    like dict of lists, but with tuples         key:value pairs with column names as
                                                keys and index-labeled key:value pairs
    column-wise                     
                                                column-wise
                                                
    + dict of series                            + list of dicts
    a continuation of key concept #2            list of key:value pairs containing column
                                                labels and values
    column-wise     
                                                row-wise
'''
# 2 - dict of series
print()
print("2 - dict of series")
series_names = pd.Series(names)
series_ages = pd.Series(ages)
series_married = pd.Series(married)
df = pd.DataFrame({'name': series_names,
                   'ages': series_ages,
                   'married': series_married})

print(df)

# 3 - dict of dicts
print()
print("3 - dict of dicts")
df = pd.DataFrame({'names': {0: 'Olga', 1: 'Andrew'}})
print(df)

# let's get all of our list into this shape; for this I am going to use a built-in python function called enumerate
# which is like an iterator with a counter-combine, so using enumerate will be able to traverse the list as well as access
# each items position at the same time.

# The enumerate function
print()
print("The enumerate function")
enumerate(names)
print(f"list: {list(enumerate(names))}")
# We are going to use a dictionary comprehension to create the key value pair
dict_names = {k: v for k, v in enumerate(names)}
dict_ages = {k: v for k, v in enumerate(ages)}
dict_married = {k: v for k, v in enumerate(married)}


# We now have three dictionaries representing each of the free columns
# in this case we copied the line dict_names to writte dict_ages and dict_married so, it should ring a bell!!!
# The code can probably be refactored

def convert_list_to_dict(l):
    return {k: v for k, v in enumerate(l)}


dict_names = convert_list_to_dict(names)
print(f"List 1 {names} transformed in Dictionary 1: {dict_names}")

dict_ages = convert_list_to_dict(ages)
print(f"List 2 {ages} transformed in Dictionary 2: {dict_ages}")

dict_married = convert_list_to_dict(married)
print(f"List 3 {married} transformed in Dictionary 3: {dict_married}")

print("Now we can create a DataFrame with the 3 Dictionary")

df = pd.DataFrame({'name': dict_names,
              'ages': dict_ages,
              'married': dict_married})

print(df)

# So far, we took a column centric approach. Let's now take a row centric approach with a list of dicts approach.
# 4 - List of dicts
print()
print('4 - list of dicts')
df = pd.DataFrame([{'name': 'Olga',
                    'age': 29,
                    'married': False}])
print(df)

# To do this efficiently let's use a zip() method
# the zip method
print()
print(list(zip(names, ages, married)))
print()
print("rowwise dictionary transformed in DataFrame")
rowwise = [{'name':name, 'age':age, 'married':married} for name, age, married in zip(names, ages, married)]
