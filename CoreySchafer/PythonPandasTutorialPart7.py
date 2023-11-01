# https://www.youtube.com/watch?v=T11QYVfZoD0&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=7

################
# Chapter 7    #
# Sorting Data #
################
people = {
    "first": ["Corey", "Jane", "John", 'Adam'],
    "last": ["Schafer", "Doe", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com", 'A@email.com']
}

import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line

df = pd.DataFrame(people)
print(df)

# last name will be sorted alphabetically, if it was numbers there'll be sorted smallest to highest
print("\n")
print(f"last name is sorted alphabetically in ascending order (default behavior):\n{df.sort_values(by='last')}")

# If we want to sort in descending order
print(f"last name is sorted alphabetically in descending order: df.sort_values(by='last', "
      f"ascending=False) \n{df.sort_values(by='last', ascending=False)}")

# If we want to sort first on last name if two values are equals then sort on first name
print(f"Last name is sorted first if two equals values we sort on first "
      f"name:\n{df.sort_values(by=['last', 'first'], ascending=False)}")

# If we want to sort ascending a column and descending another column?
print("sorting first columnn in ascending order and last column in descending order")
df.sort_values(by=['last', 'first'], ascending=[False, True], inplace=True)
print(df)

# If we want to sort on index
print(df.sort_index())

# If we want to sort a single column we can sort a serie (single column = serie)
print("\n")
print(f"If we want to sort a single column we can sort a serie "
      f"(single column = serie) df['last'].sort_values():\n{df['last'].sort_values()}")

# Let's sort the survey result
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df.sort_values(by='Country', inplace=True)
print("\n")
print(f"Sort the country columns and only print the first 50 lines with df['Country'].head(50):\n{df['Country'].head(50)}")

# Let's sort on Country and ConvertedComp in ascending, descending order and get the first 50 lines
print("\n")
df.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False], inplace=True)
print(f"Sort on Country and ConvertedComp in ascending, descending order and get the first "
      f"50 lines "
      f"df.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False], inplace=True):"
      f"\n{df[['Country', 'ConvertedComp']].head(50)}")

# There is a much simpler way to do the above
print("\n")
print("----------------------------------------------------------------------------------------------------------------")
print(f"There is a much simpler way to do the above:\n{df['ConvertedComp'].nlargest(10).head(50)}")
print("\n")
print("----------------------------------------------------------------------------------------------------------------")
print(f"the tenth largest salary: {df.nlargest(10, 'ConvertedComp')['ConvertedComp']}")
print("\n")
print("----------------------------------------------------------------------------------------------------------------")
print(f"the tenth smallest salary: {df.nsmallest(10, 'ConvertedComp')['ConvertedComp']}")