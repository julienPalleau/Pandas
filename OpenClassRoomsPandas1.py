# https://openclassrooms.com/fr/courses/7410486-nettoyez-et-analysez-votre-jeu-de-donnees/7451506-nettoyez-vos-donnees-avec-python

# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np
import re


# Chargement et affichage des donnees
data = pd.read_csv('personnes.csv')
print(data)
print(data.columns)

# Detectez les erreurs
print(data.isnull().sum())

print("\n")
print(data.loc[data['email'].duplicated(keep=False),:])

# Traitez les pays
VALID_COUNTRIES = ['France', 'Côte d\'ivoire', 'Madagascar', 'Bénin', 'Allemagne'
                  , 'USA']
mask = ~data['pays'].isin(VALID_COUNTRIES)
data.loc[mask, 'pays'] = np.NaN
print("\n")
print(data)

# Traitez les emails
data['email'] = data['email'].str.split(',', n=1, expand=True)[0]
print("\n")
print(data)

# Traitez les tailles
data['taille'] = data['taille'].str[:-1]
data['taille'] = pd.to_numeric(data['taille'], errors='coerce')
print("\n")
print(data)

# Traitez les dates
data['date_naissance'] = pd.to_datetime(data['date_naissance'], format='%d/%m/%Y', errors='coerce')
# Plus de doc sur datetime: https://docs.python.org/fr/3/library/datetime.html#strftime-and-strptime-format-codes