# https://www.youtube.com/watch?v=HQ6XO9eT-fc&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=6

############################################################################
# Chapter 6                                                                #
# Add/Remove Rows and Columns From DataFrames                              #
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

# Let's say we want to combine our first name and last name column
print(f"combine our first name and last name column: \n{df['first'] + ' ' + df['last']}")

print("\n")
df['full_name'] = df['first'] + ' ' + df['last']
print(f"Create a new column full_name that will contain combination of first and last name: \n{df}")

# Let's drop columns
print("\n")
df.drop(columns=['first', 'last'], inplace=True)
print(df)

# if we wanted to reverse that process and split that full name column in two different columns:
print("\n")
print(df['full_name'].str.split(' ', expand=True))

print("\n")
df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)
print(f"we reversed the process in splitting the full_name columns in two different columns first and last:\n{df}")

# Let's look at adding rows of data
# First let's add a single row of data
# pandas >= 2.0: append has been removed, use pd.concat
print("\n")
df2 = pd.DataFrame(['first', 'Tony'])
df = pd.concat([df, df2], ignore_index=True)
print(df)


people = {
    "first": ["Corey", "Steve"],
    "last": ["Stark", "Rogers"],
    "email": ["IronMan@avenge.com", "Cap@avenge.com"]
}
df2 = pd.DataFrame(people)
print("\n")
print(f"our new dataframe is:\n{df2}")

df=pd.concat([df, df2], ignore_index=True, sort=False)
print("\n")
print(df)

# Let's look at remonving rows
# example1:
print("\n")
df.drop(index=[3, 4], inplace=True)
print(df)

# example2:
print("\n")
filt = df['last'] == 'Doe'
# the two lines below do the same the second one is more readable as filt = df['last'] == 'Doe'
df.drop(index=df[df['last'] == 'Doe'].index)
df.drop(index=df[filt].index, inplace=True)
print(df)