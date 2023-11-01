# https://www.youtube.com/watch?v=W9XjRYFkkyw&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=3

################################################
# Chapter 3                                    #
# Indexes - How to Set, Reset, and Use Indexes #
################################################

import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 1000)

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}

df = pd.DataFrame(people)
print(df)

# If i want to view all the email addresses
print("\n")
print(f"If i want to view all the email addresses:\n {df['email']}")

# What if we wanted to set the email addresses as indexes?
print("\n")
df.set_index('email', inplace=True)
print(f"What if we wanted to set the email addresses as indexes?:\n {df}")

print("\n")
print(df.loc['CoreyMSchafer@gmail.com', 'last'])

# After we changed the index if we try
# df.loc[0] it will fail
# df.iloc[0] still work as expected
# If we set_index and want to reset it:
df.reset_index(inplace=True)
print(f"we can see that index has been reseted {df}")

# Let's set the index when loading the data file:
print("\n")
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')
print(f"we can see that we have Respondent column as index:\n{df.head()}")

# Let's have a look at our schema:
print("\n")
print(f"df schema:\n {schema_df}")

# What if we want to know what a column means without printing the all schema?
print("\n")
print(
    f"What if we want to know what a column means without printing the all schema?:\n{schema_df.loc['MgrIdiot', 'QuestionText']}")
print(f"Sort the index alphabetically:\n{schema_df.sort_index()}")
print("\n")
print(f"Sort the index alphabetically in descending order:\n{schema_df.sort_index(ascending=False)}")

# Above the DF hasn't been modified. If we want the DF to be modified:
schema_df.sort_index(inplace=True)
print(
    f"Above the DF hasn't been modified. If we want the DF to be modified: schema_df.sort_index(inplace=True)\n{schema_df}")