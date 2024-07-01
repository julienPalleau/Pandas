# import pandas as pd
# user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
# users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols, index_col='user_id')
# print(f"zip code duplicated: {users.zip_code.duplicated().sum()}")
# print(f"user duplicated: {users.duplicated().sum()}")
# print("Before we drop the duplicated lines:")
# print(users.shape)
# print()
#
# print("After we dropped the duplicated lines")
# # We drop all the duplicated lines
# #print(users.loc[users.duplicated(keep=False), :])
#
# # We keep the first duplicated line and drop the others arriving after the first one.
# print()
# users.drop_duplicates(keep='first', inplace=True)
# print(users)
# print(users.shape)
#
# # We drop lines but when we have a duplicated value in the column zip.code
# print()
# print(f"zip code duplicated after we removed the duplicated zip code: {users.drop_duplicates(subset=['zip_code'], keep='first').duplicated().sum()}")
# print(users.shape)
# ---------------------
# import pandas as pd
#
# argument_1 = 3
#
#
# def factoriel(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factoriel(n - 1)
#
#
# print(factoriel(3))
