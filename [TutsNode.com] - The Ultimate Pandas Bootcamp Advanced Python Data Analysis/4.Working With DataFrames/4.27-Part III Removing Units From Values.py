# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames
import io
import pandas as pd
import requests

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 9000)

url = 'https://andybek.com/pandas-nutrition'
s = requests.get(url).content
nutrition = pd.read_csv(io.StringIO(s.decode("utf-8")), index_col='name')  # we position the index column on name column

nutrition.replace('[a-zA-Z]', '', regex=True, inplace=True)
print(nutrition.head())

# Let's convert all the values in float in order to sum them up.
nutrition = nutrition.astype(float)
print(nutrition.total_fat.sum())
print(nutrition.info(verbose=False))