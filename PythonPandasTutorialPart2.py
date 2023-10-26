# https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=2
# Python Pandas Tutorial (Part2): DataFrame and Series Basics - Selecting Rows and Columns

#############
# Chapter 1 #
#############

import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 1000)

print(df.head())
print(df.head(5))
print(df.head())
print(df.tail(10))
print(schema_df)

#############
# Chapter 2 #
#############

# Creation of a DataFrame from a dictionary
people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}
df = pd.DataFrame(people)

# How to look at our DataFrame
# Two syntaxes are possible to look a column but prefere the first one with []
print("\n")
print(df)
print("\n")
print(df['email'])
print(df.email)

# Look at multiple columns of our DF (a DF as more than 1 column otherwise it is a serie)
print("\n")
print(df[['last', 'email']])

# look at columns name
print("\n")
print(f'columns name: {df.columns}')

################
# ILOC and LOC #
################
# look at rows with loc and iloc(integer location)
print("\n")
print(f"look at the first row with df.iloc[0]:\n{df.iloc[0]}")

# Like we were able to look at multiple columns we can look at multiple rows for instance 1st and 2nd row:
print("\n")
print(f"we can look at multiple rows for instance 1st and 2nd row:\n{df.iloc[[0, 1]]}")

# I can look at the email by looking at columns like this:
print("\n")
print(f"I can look at the email by looking at columns like this: df.iloc[[0, 1], 2]:\n {df.iloc[[0, 1], 2]}")
print("I look at line 0 and 1 and at column 2 -> email")

# For now loc seems to be the same as iloc but patience!
print("\n")
print(df)
print("\n")
print(df.loc[0])
print("\n")

# Like with iloc we can print multiple rows for instance first and second row:
print(df.loc[[0, 1]])

# Just like with iloc we can pass a second value to select a column as we use loc we can use the column name: email:
print("\n")
print(
    f"Just like with iloc we can pass a second value to select a column as we use loc we can use the column name: email:\n{df.loc[[0, 1], 'email']}")
print("\n")
print(f"Like with iloc we can have multiple columns name:\n{df.loc[[0, 1], ['email', 'last']]}")

# Let's check the number of rows and columns, we already saw how to do that:
print("\n")
df = pd.read_csv('data/survey_results_public.csv')
print(f"number of rows and columns {df.shape}")

# Again to see all the columns available
print(df.columns)

# Lets look at a specicific column like Hobbyist
print("\n")
print(f"Lets look at a specicific column like Hobbyist: {df['Hobbyist']}")

# In the result above how many Yes do we have and how many No do we have?
print(f"Numer of Yes and No in the result returned by df ['Hobbyist']: {df['Hobbyist'].value_counts()}")

# Let's grab a specific row and a sapecifi column
print("\n")
print(f"Result for line 0 and column Hobbyist we do df.loc[0, 'Hobbyist']: {df.loc[0, 'Hobbyist']}")
print("\n")
print(f"To see the first 3 responses we do df.loc[[0,1,2], 'Hobbyist]':\n{df.loc[[0, 1, 2], 'Hobbyist']}")

# Let's do the same but with slicing
print("\n")
print(df.loc[0:2, 'Hobbyist'])

# Let's do it again but with slicing columns as well
print("\n")
print(f"Let's do it again but with slicing columns as well:\n{df.loc[0:2, 'Hobbyist': 'Employment']}")

#############
# Chapter 3 #
#############
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
print(f"What if we want to know what a column means without printing the all schema?:\n{schema_df.loc['MgrIdiot', 'QuestionText']}")
print(f"Sort the index alphabetically:\n{schema_df.sort_index()}")
print("\n")
print(f"Sort the index alphabetically in descending order:\n{schema_df.sort_index(ascending=False)}")

# Above the DF hasn't been modified. If we want the DF to be modified:
schema_df.sort_index(inplace=True)
print(f"Above the DF hasn't been modified. If we want the DF to be modified: schema_df.sort_index(inplace=True)\n{schema_df}")

#############
# Chapter 4 #
#############
