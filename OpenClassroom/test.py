# import numpy as np
# import pandas as pd
# import requests
#
# pet_store_data = [
#     {
#         "dog": 17,
#         "cat": 4,
#         "rabbit": 8
#     },
#     {
#         "lizard": 1,
#         "snake": 4,
#         "dragon": 2
#     },
#     {
#         "fish": 20,
#         "frog": 6,
#         "toad": 1
#     }
# ]
#
# # ne fonctionne pas
# # total_animal_numbers = list(pet_store_data.items())
# # print(f'Total number of animals in pet store: {sum(total_animal_numbers)}')
#
# total_animal_numbers = [int(v) for dct in pet_store_data for k, v in dct.items()]
# print(total_animal_numbers)
# print(f'Total number of animals in pet store: {sum(total_animal_numbers)}')
#
# d = {1: '001', 2: '010', 3: '011'}
# # since 4 is not in keys, it'll print "Not found"
#
# test = f"{d.get('units', 'Not found')}"
# print(test)
#
# # ------------
# print("\n")
#
# ex_list = [1, 2, 3, 4]
#
#
# def get_square(lst):
#     new_lst = []
#     for num in lst:
#         new_lst.append(num ** 2)
#     return new_lst
#
#
# result = get_square(ex_list)
# print(f"resultat de get_square(): {result}")
#
#
# def get_square(lst):
#     for num in lst:
#         yield num ** 2
#
#
# result = get_square(ex_list)
# # methode 1
# print(result)
# print(f"Methode 1: On itere sur ce qui est renvoye par get_square() et on affiche")
# for num in result:
#     print(num**2)
#
# # methode 2
# print(f"Methode 2: On peut creer une liste: {list(get_square(ex_list))}")
#
# # methode 3
# result = get_square(ex_list)
# print(f"Methode 3: Every iterator object in Python defines a next method"
#       f" next(result), The next method returns the next item in the iterator until all items are over in which case it throws a StopIteration Error): "
#       f"\n{next(result)**2}\n{next(result)**2}\n{next(result)**2}\n{next(result)**2}\n")
#
# # method 4
# # list comprehension
# result = [x**2 for x in range(4)]
# print(result)
#
# # to convert the line above into a generator:
# result = (x**2 for x in range(4))
# print(result)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
#
# # Once again I can convert the result to a list
# result = (x**2 for x in range(4))
# print(list(result))


# Union operator
# | for union
# & for intersection
# - for difference
# ^ for symmetric difference
cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}
cities_jp = {'Tokyo': 'JP'}

cities = cities_us | cities_uk | cities_jp

print(cities)
