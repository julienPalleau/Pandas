# https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=2
# Python Pandas Tutorial (Part2): DataFrame and Series Basics - Selecting Rows and Columns

############################################################
# Chapter 2                                                #
# DataFrame and Series Basics - Selecting Rows and Columns #
############################################################

import pandas as pd
pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line


df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')


print(df.head())
print(df.head(5))
print(df.head())
print(df.tail(10))
print(schema_df.to_string())

###############
# Chapter 2   #
###############

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
print(f"Let's do it again but with slicing columns as well:\n{df.loc[0:2, 'Hobbyist': 'Employment'].to_string()}")




