import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)
data = pd.read_csv("clients.csv")

print(data.columns)
print(data.iloc[10:20, 1: 3])
print(data.iloc[10:20, [1, 3]])