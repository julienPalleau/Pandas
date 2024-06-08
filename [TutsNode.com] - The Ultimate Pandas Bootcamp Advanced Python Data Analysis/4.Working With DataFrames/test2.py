import pandas as pd

data = ['Julien', 'Lucie', 'Tom']
ages = [27, 49, 37]
frame = {'Name': pd.Series(data),
         'Age': pd.Series(ages)}
df_test = pd.DataFrame(frame)
df_test.loc[-1] = ['eliott', 33]
df_test = df_test.sort_index()

print(df_test)