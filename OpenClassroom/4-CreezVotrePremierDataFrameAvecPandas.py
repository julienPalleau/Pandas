# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857178-creez-votre-premier-data-frame-avec-pandas
import pandas as pd

pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)

# Chargement du fichier
data = pd.read_csv("clients.csv")

# afficher les 5 premieres lignes
print(data.head())

# afficher les 2 dernieres lignes
print(data.tail(2))

# afficher les 5 premieres et dernieres lignes
print(data)

# Caracteristiques globales du data frame
print(f"Caracteristiques globales du data frame data.shape data.shape[0] lignes x data.shape[1] colonnes: {data.shape} {data.shape[0]} lignes x {data.shape[1]} colonnes")

# Connaitre les types d'un data frame:
print(f"Connaitre les types d'un data frame data.dtypes: {data.dtypes}")
# En Pandas le type objet correspond en fait à une colonne de type chaine de caractere (ou string).

clients_array = data.values
print(clients_array)