# https://www.youtube.com/watch?v=Lw2rlcxScZY&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=4

#############################################################
# Chapter 4                                                 #
# Filtering - Using Conditionals to Filter Rows and Columns #
#############################################################

import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

pd.options.display.max_columns = 0
pd.set_option('display.max_columns', 3000)
pd.set_option('display.max_rows', 3000)



people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}
df = pd.DataFrame(people)

# Let's filter our result, so we want all the lines with Doe in the email column
print("\n")
print(f"Let's filter our result, so we want all the lines with Doe in the email column:\n {df['last'] == 'Doe'}")
# The results are boolean values True or False and this result is called a mask
# Let's use the mask as a filter mask
filt = (df['last'] == 'Doe')

# We can use it in different way:
# 1st way
print(df[filt])

# 2nd way
print(df[df['last'] == 'Doe'])

# 3rd way
print("\n")
print(
    f"df.loc[filt, 'email'], First value are the rows that we want,  second value are the columns that we want:\n{df.loc[filt, 'email']}")

# Using & and | to create complex filter
# If we want all the rows where the last name is equal to Doe and the first name is equal to John
filt = (df['last'] == 'Doe') & (df['first'] == 'John')
print(
    f"Let's create a complex filter using & (df['last'] == 'Doe') & (df['first'] == 'John'):\n{df.loc[filt, 'email']}")

# Now let's look at an example wiht |
filt = (df['last'] == 'Schafer') | (df['first'] == 'John')
print(
    f"Let's create a complex filter using | (df['last'] == 'Schafer') | (df['first'] == 'John'):\n{df.loc[filt, 'email']}")

# We can also get the opposit of a filter, Let's say we want the opposite of the previous request,
# so we want everything which doesn't have schafer as a last name and John as a first name
print(f"This the opposite of the previous request df.loc[~filt, 'email']:\n{df.loc[~filt, 'email']}")

# Let's have a look to people with a salary above a certain amount
print("\n")
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
high_salary = (df['ConvertedComp'] > 70000)
print(
    f"Filter on high salary with high_salary = df.loc[(df['ConvertedComp'] > 70000) and printing only columns, "
    f"Country, LanguageWorkedWith and ConvertedComp:"
    f"\n{df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]}")

# Let's create a filter on multiple countries
countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
filt = df['Country'].isin(countries)
print("\n")
print(f"Filter on multiple countries but only print country column:\n{df.loc[filt, 'Country']}")

# In looking at LanguageWorkedWith we can see: C++;HTML/CSS;Java;JavaScript;Python;SQL;VBA
print("\n")
print(df['LanguageWorkedWith'])
# so how to proceed to check if a language is there?
# Let's re-write the filter
filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
print(df.loc[filt, 'LanguageWorkedWith'])