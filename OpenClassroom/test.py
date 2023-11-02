import pandas as pd
import requests

# pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)
# data = pd.read_csv("clients.csv")
#
# print(data.columns)
# print(data.iloc[10:20, 1: 3])
# print(data.iloc[10:20, [1, 3]])

response = requests.get('https://www.google.com/')
if not len(response.text.strip()) > 0:
    print(f"La variable request est vide.")
else:
    print(f"La variable request n'est pas vide.")

print(response.text)