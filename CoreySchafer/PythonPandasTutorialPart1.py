# https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=1
######################################################################
# Chapter 1                                 #
# Getting Started with Data Analysis - Installation and Loading Data #
######################################################################

import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line

df = pd.read_csv('data/survey_results_public.csv')
print(df.shape)  # give us the number of lines and columns
print(df.info())  # gives us number of lines and columns but also the detail of each columns and their data types

schema_df = pd.read_csv('data/survey_results_schema.csv')
print(schema_df)

print(schema_df.head())  # gives the first 5 rows
print(schema_df.head(10))  # gives us the first 10 rows
print(schema_df.tail(10))  # gives us the last 10 rows
