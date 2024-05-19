# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
import pandas
import pandas as pd

#Q1
print("Exercice 1")
actor_names = ['John Depp', 'Matthew McConaughey', 'Pierre Ninez', 'Vincent Rottiers']
print(len(actor_names))

#Q2
print("Exercice 2")
actor_ages = [44, 48, 30, 32]
actor_names_and_age = pd.Series(data=actor_ages, index=actor_names, name='actors')
# actor_names_and_age.name='actors'
actor_names_and_age.index.name="actors'  name"
print(actor_names_and_age)
print()

#Q3
print("Exercice 3")
print("Exercice 3 - Solution manuelle")
dict_actor_name_and_age = {'John Depp' : 44, 'Matthew McConaughey': 48, 'Pierre Ninez': 30, 'Vincent Rottiers': 32}
actor_names_and_age = pd.Series(dict_actor_name_and_age)
print(actor_names_and_age)

# la meme chose que ci-dessus, mais sans le faire manuellement
print()
print("Exercice 3 - sans taper le dictionnaire")
print(pd.Series(dict(zip(actor_names, actor_names_and_age))))

print()
print("Exercice 3 - Une autre solution")
# Another solution with dictionary comprehension
print(pd.Series({name: age for name, age in zip(actor_names, actor_names_and_age)}))