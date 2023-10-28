# https://www.youtube.com/watch?v=T11QYVfZoD0&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=7

################
# Chapter 7    #
# Sorting Data #
################
people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}

import pandas as pd

df = pd.DataFrame(people)
print(df)