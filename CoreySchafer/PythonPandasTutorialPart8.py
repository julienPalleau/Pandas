# https://www.youtube.com/watch?v=txMdrV1Ut64&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=8

################################################################
# Chapter 8                                                    #
# Grouping and Aggregating - Analyzing and Exploring Your Data #
################################################################

import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line

df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)

# Let's have a look at the sarlary(ConvertedComp) median
print(df['ConvertedComp'].head(15))
print("\n")
print(f"Median salary {df['ConvertedComp'].median()}")

# Now we want to get median salary by country:
# First let's have a look at how run aggregate function on our DataFrame
print("\n")
# in the output of describe() the count value represents the number of peope who answered the question
# in other words count returns the number of non NA
# !!! If you want the number of individual values then you must not look at count you must look at value_count !!!
print(df.describe())

# if we look at the Hobbyist column and want to see how many answered Yes and how many answered No
print("\n")
print(f"How many answered Yes and how many answered No df['Hobbyist'].value_counts(): \n{df['Hobbyist'].value_counts()}")

print("\n")
# Let's have a look to SocialMedia column
print(df['SocialMedia'])
print("\n")
# If we want to know the exact question about SocialMedia, we have to look at the schema_df
print(schema_df.loc['SocialMedia'])
print(df['SocialMedia'].value_counts())
# If we want the result above in percentage
print(f"Same result as above but in % df['SocialMedia'].value_counts(normalize=True)"
      f":\n{df['SocialMedia'].value_counts(normalize=True)}")

# First, let's have a look at the number of answers by country
print("\n")
print(f"number of answers by country df['Country'].value_counts(): \n{df['Country'].value_counts()}")

# Secondly, How do we break up those results by country?
country_grp = df.groupby(['Country'])
print(f"How do we break up those results by country?: \n{country_grp.get_group('United States')['Country']}")

# I could have done something similar with filter
filt = df['Country'] == 'United States'
print(f"I could have done the same as above with "
      f"filt = df['Country'] == 'United States', df.loc[filt]['Country']: \n{df.loc[filt]['Country']}")
# but using filter gives us result for one coutry while groupby split result by country for all countries

# Let's look at most popular social media web site broken down per country
print("\n")
print(f"Let's look at most popular social media site per country "
      f"country_grp['SocialMedia'].value_counts().head(50):\n {country_grp['SocialMedia'].value_counts().head(50)}")

# If I want the most popuplar social media web site for one country:
# normalize=True is to get results in %
print(f"the most popuplar social media web site for one country "
      f"country_grp['SocialMedia'].value_counts().loc['India']:\n "
      f"{country_grp['SocialMedia'].value_counts(normalize=True).loc['India']}")

# Now let's have a look at the median salary per country
print("\n")
print(f"median salary per country: \n{country_grp['ConvertedComp'].median().head(50)}")

# If I want the salay for a specific country
print(f"The salay for a specific country (Germany): \n{country_grp['ConvertedComp'].median().loc['Germany']}")

# Let's say we don't want to see jut the median but we also want to see the mean
print(f"We want to see the median and the mean: \n{country_grp['ConvertedComp'].agg(['median', 'mean'])}")

# If i want to look at the mean and median salary for canada
print(f"mean and median salary for canada: \n{country_grp['ConvertedComp'].agg(['median', 'mean']).loc['Canada']}")

# The languade people work with break down by country
print("\n")
print(f"The languade people work with break down by country: "
      f"country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum(): "
      f"\n{country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())}")

# We want to know the % of developpers who knows python for each country
# To do that we will use a combination of few different things that we saw so far
# 1) First we grab the total number of people for each country who responded to the survey
country_respondents = df['Country'].value_counts()
print(country_respondents)
# 2) Secondly we grab the total number of people who knows Python in each country
country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
print(country_uses_python)
# 3) So now we have one variable country_respondents which is a serie and another variable country_uses_python which
# is a serie, so to get the % we need to combine those two variables.
python_df = pd.concat([country_respondents, country_uses_python], axis='columns')
python_df.rename(columns={'count': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)
print(f"{python_df}")
# 4) now we create a new column and compute the %
python_df['PctKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents']) * 100
python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)
print(f"------------------")
print(f"% of people who knows python in a developper population by country: \n{python_df.head(50)}")
# 5) Let's have a look to a specific country
print("\n")
print(python_df.loc['Japan'])
