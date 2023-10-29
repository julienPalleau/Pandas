# https://www.youtube.com/watch?v=KdmPHEnPJPs&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=9

#################################################################
# Chapter 9                                                     #
# Cleaning Data - Casting Datatypes and Handling Missing Values #
#################################################################

import pandas as pd
import numpy as np

people = {
    "first": ["Corey", "Jane", "John", 'Chris', np.nan, None, 'NA'],
    "last": ["Schafer", "Doe", "Doe", "Schafer", np.nan, np.nan, 'Missing'],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com", None, np.nan, "Anonymous@email.com", "NA"],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
df = pd.DataFrame(people)
print(df)