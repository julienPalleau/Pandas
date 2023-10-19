# https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=2
# Python Pandas Tutorial (Part2): DataFrame and Series Basics - Selecting Rows and Columns

import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

print(df.head())