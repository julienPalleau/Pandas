import pandas as pd
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col='user_id')
print(users.zip_code.duplicated().sum())
print(users.duplicated().sum())
print(users.loc[users.duplicated(keep=False), :])
print(users.drop_duplicates(keep='first', inplace=True))
print(users.shape)