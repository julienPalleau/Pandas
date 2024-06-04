#W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames

import io
import pandas as pd
import requests

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',50)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")))
print(nutrition.head(10))
print(nutrition.info(verbose=False, memory_usage='deep'))
print()

# Let's have a look at the column 'Unnamed: 0' as it provides the same information as index.
print(nutrition['Unnamed: 0'])

# Let's remove the column 'Unnamed: 0' to do that we have a couple of options
# 1 - Obviously one is to just drop this column, so starting with the DataFrame
print(nutrition.drop('Unnamed: 0', axis=1))
print()
print('---')

# 2 - Another approach is to designate that unwanted column as the index after we have erading the data so, instead of filling it or dropping it
# we simply specify as index
nutrition.set_index('Unnamed: 0')
print(nutrition)

# 3 - Load the data in selecting the index column (prefered solution)
print()
url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col=0)
print(nutrition)