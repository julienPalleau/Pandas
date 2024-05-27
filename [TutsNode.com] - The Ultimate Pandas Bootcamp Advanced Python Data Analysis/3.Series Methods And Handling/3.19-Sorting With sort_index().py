# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\3. Series Methods And Handling
import pandas as pd

alcohool = pd.read_csv('drinks.csv', usecols=['country', 'wine_servings'], index_col='country')
alcohool = alcohool.squeeze('columns')

print(alcohool.head())
print()
res = alcohool.sort_index(ascending=False, na_position='first', inplace=True)
print(alcohool)
print()
print(f"Number of null values: {alcohool.index.isnull().sum()}")

'''
            sort_values() & sort_index()
    
    sort_values(): returns a new series, sorted by values
    sort_index(): returns a series, sorted by index labels
    
        Default Params:     ascending=True
                            inplace=False
                            na_position='last'
                            kind='quicksort'

'''