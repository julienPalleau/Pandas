# https://www.youtube.com/watch?v=KdmPHEnPJPs&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=9

#################################################################
# Chapter 9                                                     #
# Cleaning Data - Casting Datatypes and Handling Missing Values #
#################################################################

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line

people = {
    "first": ["Corey", "Jane", "John", 'Chris', np.nan, None, 'NA'],
    "last": ["Schafer", "Doe", "Doe", "Schafer", np.nan, np.nan, 'Missing'],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com", None, np.nan, "Anonymous@email.com", "NA"],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
df = pd.DataFrame(people)
print(df)

# In this exercise we will drop the incomplete lines
print(f"we drop the incomplete lines:\n{df.dropna(axis='index', how='any')}")
print("")
print(f"we drop the line full of NaN (line 4):\n{df.dropna(axis='index', how='all')}")
# df.dropna use by default df.dropna(axis='index', how='any')
# 1 - the first argument "axis" can be set to "index" or "columns", if it is set to index it means we will drop our rows when we have a Na value in it
#     if it is set to "columns" it means we will drop columns when we have a Na value in it
# 2 - the second argument "how" is how we want to drop or a better way to find that is this is the criteria that is used for dropping a row or a column.
#     as this is set to "any", it will drop rows with any missing values.
#     we could have df.dropna(axis='index', how='all') this would then only drop rows when all the values in that row are missing.

# if we use df.dropna(qxis='columns', how='all')
print("\n")
print(f"we drop a column only if the column is full of Na (axis='columns', how='all'):\n{df.dropna(axis='columns', how='all')}")

# if use df.dropna(qxis='columns', how='any'), we got nothing
print("\n")
print(f"if use df.dropna(qxis='columns', how='any'), we got nothing:\n{df.dropna(axis='columns', how='any')}")

# If we do somme analysis on our data and it's fine if they don't have a first name or a last name but we really need the email address and if they don't have an email
# address then we just need to drop those rows. In order to do this we can pass a subset argument.
print("\n")
# with df.dropna(axis='index', how='any', subset=['email']) we remove Na only in column email, we still get line 6 as this is not Na but NA
print(f"{df.dropna(axis='index', how='any', subset=['email'])}")

# we can pass multiple columns let's say last and email, and if we have on a row NaN in those two columns it will be dropped.
print("\n")
print(f"we can pass multiple columns let's say last and email, and if we have on a row NaN in those two columns it will be dropped.:"
      f"\n{df.dropna(axis='index', how='all', subset=['last', 'email'])}")

# Let's have a look to customise missing values like NA, Missing
# we can replace those custom values with proper np.NaN numpy value while loading the data in the DataFrame
print("\n")
df = pd.DataFrame(people)
df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)
print(df)

# to see if value will be treated as na we can just run a mask like this:
print(df.isna())

# Sometimes especially when working with numerical data, we might want to fill our na value with a particular value.
print("\n")
print(df.fillna('MISSING'))
print(df.fillna(0))

# Let's say we want to get the average age of all the people in this sample data frame
# First let's look at DataFrame types
print(f"let's look at our DataFrame types: \n{df.dtypes}")
# np.nan is a float
print(f"np.nan type is: {type(np.nan)}")
# so we can see from the result of the line above is that age is not a numeric but a string
df['age'] = df['age'].astype(float)
print(df.dtypes)
print(df['age'].mean())

# Replacing the custom values but this time in loading a csv file
na_vals = ['NA', 'Missing']
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent', na_values=na_vals)
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

# Let's have a look at the experience of developpers in looking at YearsCode
print(f"{df['YearsCode'].head(10)}")

# To see all the unique value from a column, and we can see we have string: Less than 1 year, and More than 50 years
print(df['YearsCode'].unique())
# So we will replace less than 1 year by 0
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)

# So we will replace more than 50 years by 51
df['YearsCode'].replace('More than 50 years', 51, inplace=True)

# Now we want to convert the new values 0 and 51 in float
df['YearsCode'] = df['YearsCode'].astype(float)

print(f"The average of coding experience in year: \n{df['YearsCode'].mean()}")
print(f"The median of coding experience in year: \n{df['YearsCode'].median()}")
