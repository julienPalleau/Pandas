# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\4. Working With DataFrames
import pandas as pd
import numpy as np

print(pd.__version__)

# some python lists
names = ['Olga', 'Andrew', 'Brian', 'Telulah', 'Nicole', 'Tilda']
ages = [29, 21, 45, 23, 39, 46]
married = [False, True, True, True, False, True]

# pandas series
ser = pd.Series(names, name='name')

# pandas dataframe
df = pd.DataFrame({'name': names, 'age': ages, 'married': married})
print(df)

# A DataFrame (abobe) is a table of data that contains collections of rows and columns.

'''
            DATAFRAMES
        First key concept

    dataframes have two                 name    age    married
    dimensions: labeled           0     Olga    29    False
    indices and columns           1     Andrew  21    True
                                  2     Brian   45    True
                                  3     Telulah 23    True
                                  4     Nicole  39    False
                                  5     Tilda   46    True


In a series if we want to access the name Brian
ser.iloc[2]

In a DataFrame if we want again to access the name Brian
df.iloc[2][0] note that start counting the column with name so the index is not a column
'''
print(f"Let's print the third element (line 2) from the serie or Brian name: {ser.iloc[2]}")
print(f"let's print the Brian again but from the DataFrame with: df.iloc[2]\n {df.iloc[2]}") # Here we print the full line 2

# .ndim
print(f"number of dimension for the serie ser: {ser.ndim}")
print(f"number of dimension for the DataFrame df: {df.ndim}")

# .shape
print(f"shape of the serie ser: {ser.shape}")
print(f"shape of the DataFrame df: {df.shape}")

# Series has one dimension where's DataFrame is two dimensional data structure
'''
            DATAFRAME
        Second key concept
        
                                        name    age   married
    each column in a              0     Olga    29    False
    dataframe is a series         1     Andrew  21    True
                                  2     Brian   45    True
                                  3     Telulah 23    True
                                  4     Nicole  39    False
                                  5     Tilda   46    True     

series is the data structure for a single column of a DataFrame. So in other words
a DataFrame is collection of series put together.
'''
print(df.name)

'''
            DATAFRAME
        Third key concept
        
                                        name    age   married
    unlike series,                  0     Olga    29    False
    dataframe could be              1     Andrew  21    True
    heterogenous                    2     Brian   45    True
                                    3     Telulah 23    True
                                    4     Nicole  39    False
                                    5     Tilda   46    True   
                                    dtype Object  int64 bool
'''
print(f"le type d'un DataFrame est une collection de type 1 par colonne car un DataFrame peut contenire plusieurs type contrairement au lists: df.dtypes:\n {df.dtypes}")
