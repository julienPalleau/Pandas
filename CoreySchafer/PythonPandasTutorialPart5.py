# https://www.youtube.com/watch?v=DCDe29sIKcE&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=5

############################################################################
# Chapter 5                                                                #
# Filtering - Updating Rows and Columns - Modifying Data Within DataFrames #
############################################################################

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}

import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line

df = pd.DataFrame(people)

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 1000)

print(df)

# Let's have a look to columns name
print("\n")
print(f"columns name:\n{df.columns}")

# How to rename all the columns
print("\n")
df.columns = ['first_name', 'last_name', 'email']
print(f"How to rename all the columns df.columns = ['first_name', 'last_name', 'email']:\n{df}")

# Let's say that we want to upper case all the column's name here
print("\n")
df.columns = [x.upper() for x in df.columns]
print(df)

# Let's say that we want to replace underscore by spaces
print("\n")
df.columns = df.columns.str.replace('_', ' ')
print(df)

# now let's put things back as it was
df.columns = [x.lower() for x in df.columns.str.replace(' ', '_')]
print("\n")
print(df)

# rename the columns
df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True)
print("\n")
print(df)

# Let's have a look at updating the data in our rows
# First let's have a look at how to update a single value
print("\n")
df.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']
print(
    f"We updated Doe by Smith and the email with this syntax df.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']:\n{df}")

# If I only wanted to change the last name and email
df.loc[2, ['last', 'email']] = ['Doe', 'JohDoe@email.com']
print(f"We only changed the last name and email:\n{df}")

# Change a single value in passing a single row and a single column
print("\n")
df.loc[2, 'last'] = 'Smith'
print(f"Change a single value in passing a single row and a single column df.loc[2, 'last'] = 'Smith':\n{df}")

# Let's change it back but with another syntax
print("\n")
df.at[2, 'last'] = 'Doe'
print(df)

# How do we update multiple rows of data at once?
print("\n")
df['email'] = df['email'].str.lower()
print(f"update multiple rows of data with df['email'].str.lower():\n{df}")

# Now let's have a look at 4 methods to do the same as above:
print("\n")
print("Now let's have a look at 4 methods to do the same as above:")
# apply
# map
# applymap has been deprecated
# replace

# 1- apply
# first example
print(f"1 - Let's have a look to email lenght using apply df['email'].apply(len):\n{df['email'].apply(len)}")


# Second example
def update_email(email):
    return email.upper()

df['email'] = df['email'].apply(update_email)
print(df)

# Third example where we want revert things back with a lambda function
df['email'] = df['email'].apply(lambda x: x.lower())
print(df)

# so we look at how apply works on series object
# so now let's look at how apply works with dataframes
print("\n")
numericalData = {10,20,30,40,50}
dfn = pd.DataFrame(numericalData)
print(dfn.apply(pd.Series.min))
print(dfn.apply(lambda x: x.min()))

# 2- apply map
# First example
# has been deprecated DataFrame.map should be used instead
print(df.map(len))

# Second example
print("\n")
print(df.map(str.lower))

# third example
# if we want to substitute a couple of our first names
# in this example we didn't specify anything for John, so we will get a NaN for John
print("\n")
print(df['first'].map({'Corey':'Chris', 'Jane': 'Mary'}))

# in using replace I don't get anymore the NaN
print("\n")
df['first'] = df['first'].replace({'Corey':'Chris', 'Jane': 'Mary'})
print(df)

print("\n")

df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)
print(df['SalaryUSD'])
print("\n")
print(df['Hobbyist'])
print(df['Hobbyist'].map({'Yes': True, 'No': False}))
df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})
print(df)