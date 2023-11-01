# https://www.youtube.com/watch?v=UFuo7EHI8zc&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=10

###########################################
# Chapter 10                              #
# Working with Dates and Time Series Data #
###########################################
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
utc=True

pd.set_option('display.max_columns', 1000, 'display.width', None, 'display.max_rows', 1000)
# If the line is truncated you can use your pandas pd.to_string() to get the full line

df = pd.read_csv('ETH_1h.csv')
print(df.head())

print(f"Dimension du tableau de travail: {df.shape} lines x columns")
print(df.describe())
print(df.dtypes)

# Official documentation on date formatting
# http://bit.ly/python-dt-fmt
# http://bit.ly/pandas-dt-fmt

# First let's convert our column date in dates as we can see that date column is a string
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
print(df['Date'])
print("\n")

# It is also possible to directly load our data in the expected format i.e:
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_format='%Y-%m-%d %I-%p')
print(df)
print("\n")
print(f"This date 2020-03-13 20:00:00 was a friday and we know that with df.loc[0, 'Date'].day_name(): \n{df.loc[0, 'Date'].day_name()}")
print("\n")

# Get the day for each date with dt class
print(df['Date'].dt.day_name())

# Let's say we want to create a new column so that we could quicly reference what day all this trades took place.
df['DayOfWeek'] = df['Date'].dt.day_name()
print(f"look at our DataFrame with a new column day of week: \n{df}")

# Now let's have a look at how we can explore our data a bit
# 1 - Let's see the earliest date
print(f"Let's see the earliest date: \n{df['Date'].min()}")
# 2 - Let's see the most recent date that I have
print(f"Let's see the most recent date that I have: \n{df['Date'].max()}")

# We can substract date it is called time delta
print(f"substraction of two dates df['Date'].max() - df['Date'].min(): \n{df['Date'].max() - df['Date'].min()}")

# Let's create a filter for date
filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
print(f"Here we use the following filter filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01')): \n{df.loc[filt]}")

# Now we can set the date column as our index since all the dates are unique
df.set_index('Date', inplace=True)
print(f"We set our date column as index with df.set_index('Date')")

# now we set the index on dates, I can look at all the 2019 data like this, and this is much simpler than writting a filter:
print(df.loc['2019'])
print("\n")

# We can also use slice for grabing dates for a specific range
print(f"we get the same result using slicing: df.sort_index().loc['2020-01':'2020-02']\n{df.sort_index().loc['2020-01':'2020-02']}")

print(f"This give us the average price at market closing:\n {df.sort_index().loc['2020-01':'2020-02']['Close'].mean()}")

# What if we want to look at these data on daily basis instead of one an hourly basis
print(f"Max value for the serie 2020-01-01: \n{df.sort_index().loc['2020-01-01']['High'].max()}")

# If i want to resample this and simply see the high value by day:
# Documentation for resampling https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
print("\n")
highs = df['High'].resample('D').max()
print(f"If i want to resample this and simply see the high value by day: \n{highs}")
print(f"Another way to find the max value for a the serie 2020-01-01: {highs['2020-01-01']}")

# Let's say that we want to plot this out for the price broken down by day
# plt.plot(highs)
# plt.show()

# What if we want to resample by week anď the average closing cost for the entire day
print(df.resample('W'))

aggregation = df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})
print(aggregation)