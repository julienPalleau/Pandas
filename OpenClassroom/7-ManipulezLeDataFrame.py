# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857439-manipulez-le-data-frame
import numpy as np
import pandas as pd

# Chargement du fichier
data = pd.read_csv("clients.csv")

print("""
###########################
# Manipulez le data frame #
###########################
Nous avons importé notre premier data frame… mais c’est loin d’être le dernier. Une fois nos données correctement importées, la suite logique va être de les manipuler à notre 
guise.

Voici un cas concret : nous souhaitons accéder à la liste de tous les e-mails des clients ayant contracté un prêt chez nous, à partir du data frameclients importé lors du chapitre 
précédent, pour créer une liste de diffusion pour des offres commerciales préférentielles. Comment faire cela avec Pandas ? C’est que je vous propose de voir à présent !
""")

print("""
###############################
# Naviguez dans le data frame #
###############################
""")
print(data['email'])
print("\n")
variables = ['nom', 'email']

print(data[variables])
print("""L’affichage est relativement “joli”, avec une organisation en tableau, où chaque colonne est explicitement nommée : c’est un data frame. De plus, les informations \
affichées en bas sont le nombre de lignes et de colonnes. C’est finalement assez logique, car nous avons sélectionné ici 2 colonnes. Etant donné qu'il n'y a au moins deux \
colonnes, ça ne peut pas être une Series.""")

# Il est possible de faire la meme chose en 1 ligne mais attention aux [[]]
print("\n")
print(data[['nom', 'email']])

print("\n")
print("""
######################################
# Decouvrez l'objet Series de Pandas #
######################################
""")
# Chaque colonne du data frame est de type Series:
print(f"Chaque colonne du data frame est de type Series type(data['email']): {type(data['email'])}")
# Il est important de différencier les deux objets. Même s'ils partagent de nombreuses méthodes, certaines sont néanmoins exclusives à l’un ou l’autre, et cela peut être une
# source d’erreur lors de l’implémentation d’analyse de données avec Python.

# Une différence évidente, mais que je me permets tout de même de noter : un data frame a 2 dimensions avec plusieurs colonnes, alors que la Series n’a qu’une seule dimension.
# Cela peut fortement vous aider lorsque vous utiliserez certaines méthodes, car vous pourrez savoir à quel type d’objet vous faites face, en vous basant sur l’affichage que vous
# avez de ce dernier.

# Documentation officielle de Pandas: https://pandas.pydata.org/docs/reference/api/pandas.Series.html

print("\n")
print("""
##########################
# Manipulez les colonnes #
##########################
Voyons quelques manipulations indispensables sur leśdata frames:
    + Creer ou supprimer une colonne
    + Renommer une colonne
    + Changer le type d'une colonne
    + Trier un data frame selon une ou plusieurs colonnes.
""")

print("\n")
print("""
##################################
# Modifiez une colonne existante #
##################################
""")
print(data['nom'])
data['nom'] = 1
print(f"Si j'execute data['nom'] = 1 cela aura deux effets : cela va modifier la variable  data  existante en remplaçant toutes les valeurs par 1, "
      f"et cela transforme également le type de la variable: \n{data['nom']}")

# Par exemple, si je souhaite modifier la colonne identifiant par elle-même multipliée par 100, je peux le faire de la façon suivante :
data['identifiant'] = data['identifiant'] * 100
print(f"si je souhaite modifier la colonne identifiant par elle-même multipliée par 100 data['identifiant']*100: \n{data['identifiant'] * 100}")
# Je peux aussi décider de la remplacer par des valeurs aléatoires entre 1 et 1 000 :
print("\n")
data['identifiant'] = np.random.randint(1, 1000, data.shape[0])
print(f"Je peux aussi décider de la remplacer par des valeurs aléatoires entre 1 et 1 000 : \n{data['identifiant']}")

print("\n")
print("""
##################################
# Creez et supprimez une colonne #
##################################
"Maintenant, comment créer une colonne ? De la même façon qu’on en modifie une. On appelle la colonne, comme si elle existait déjà, et on lui attribue une valeur."
"data['id'] = data['identifiant'] + 1000"
""")
# reinitialisation
data = pd.read_csv("clients.csv")
data['id'] = data['identifiant'] + 1000
print(data.head())

# Pour résumer, que ce soit pour modifier ou créer une colonne col, la syntaxe sera :  mon_dataframe['col'] = x  où x représente soit une valeur fixe, soit un objet de même
# dimension que la colonne qu’on souhaite modifier/créer.

# Et pour supprimer une colonne existante ?
# Il existe officiellement 3 façons.
# 1 - D’abord la méthode .drop des data frames :
data.drop(columns='id')
# Contrairement au deux options suivantes, la méthode.drop ne modifie pas le data frame existant, elle renvoie juste une sorte de copie du data frame en y ayant appliqué les
# modifications – ici supprimer la colonne id. Vous aurez besoin de remplacer votre data frame pour pallier cela :  data = data.drop(columns='id')  .

# - 2 La methode del:
print("\n")
del data['id']
print(f"la medthode del, del data['id']: \n{data.head()}")

# - 3 La methode pop:
# ici on recharge la colonne id afin de pouvoir la re-supprimer
print("\n")
data['id'] = data['identifiant'] + 1000
data.pop('id')
print(f"la medthode pop, data.pop['id']: \n{data.head()}")

print("\n")
print("""
########################
# Renommez une colonne #
########################
La méthode pour renommer une colonne est.rename . On peut ainsi renommer une ou plusieurs colonnes via la syntaxe :  mon_dataframe.rename(columns={'ancien nom': 'nouveau nom'}).
Voilà par exemple comment renommer la colonne identifiant en ide :
data.rename(columns={'identifiant': 'ide'})
On peut naturellement renommer plusieurs colonnes en une fois. Par exemple en modifiant  email enmail :
À noter que la méthode rename ne modifie pas le data frame existant. Il existe cependant un argument pour cette méthode (et pour toutes les méthodes similaires) nommé  
inplace, qu’il suffit de fixer à Vrai (True ) pour pallier cela. Ainsi,  data.rename(columns={'identifiant': 'ide'}, inplace=True)  est strictement équivalent à  
data = data.rename(columns={'identifiant': 'ide'}).""")

data.rename(columns={'identifiant': 'ide', 'email': 'mail'})
print("\n")
print("""
#################################
# Changez le type d'une colonne #
################################
La méthode.astype permet de changer le type d’une colonne. Par exemple, si on souhaite transformer la colonne identifiant , initialement composée d'entiers, en nombres décimaux, 
on peut le faire de la façon suivante :
""")
print(f"data['identifiant'].astype(float): \n{data['identifiant'].astype(float)}")

print("\n")
print("""
#######################
# Triez un data frame #
#######################
En analyse de données, on a régulièrement besoin de trier des données selon une ou plusieurs colonnes. Pandas met à disposition la méthode.sort_values pour faire cela 
très aisément. Il suffit de préciser entre parenthèses la ou les colonnes selon lesquelles il faut trier. Voici quelques exemples :

trier selon l'identifiant, par ordre croissant avec data.sort_values('identifiant'): """)
print(data.sort_values('identifiant'))

print("trier selon l’identifiant par ordre décroissant data.sort_values('identifiant', ascending = False):")
print(data.sort_values('identifiant', ascending=False))

print("trier selon le genre puis le nom, par ordre croissant data.sort_values(['genre', 'nom']):")
print(data.sort_values(['genre', 'nom']))

print("\n")
print("""
Comment procéder si on souhaite avoir l’un par ordre croissant et l’autre par ordre décroissant ?
Il faudra dans ce cas donner en paramètre àascending une liste de booléens. Voici par exemple comment trier par genre en ordre croissant et par nom en ordre décroissant :
data.sort_values(['genre', 'nom'], ascending=[True, False])
""")
print(data.sort_values(['genre', 'nom'], ascending=[True, False]))

############
# Exercice #
############
"""
Manipulez un dataframe

Nous allons travailler à présent sur notre fichier de prêts immobiliers.

Pour expliquer rapidement ce fichier, chaque ligne correspond à un prêt qui a été accordé à un de nos clients. Chaque client est identifié par… son identifiant ! Nous avons les 
informations suivantes :

    la ville et le code postale de l’agence où le client a contracté le prêt
    le revenu mensuel du client
    les mensualités remboursées par le client
    la durée du prêt contracté, en nombre de mois
    le type de prêt
    et enfin le taux d’intérêt

Votre rôle cette fois ci va être de modifier ce jeu de données pour calculer différentes variables nécessaires pour identifier les clients qui sont à la limite de leur capacité de 
remboursement et déterminer les bénéfices réalisées par la banque.
"""
import numpy as np
import pandas as pd

"""
Commençons par importer notre fichier csv. Celui ci sera disponible via un lien, pour faciliter le bon fonctionnement avec Google Colab, mais promis, c'est le même fichier que 
celui que vous pouvez télécharger sur le lien suivant (click droit, enregistrer sous)
"""
prets = pd.read_csv("https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv")
print(prets.info(memory_usage='deep'))
print(prets.head())

print("\n")
pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)
print(data.head())

"""
Dans un premier temps, créez une nouvelle variable calculant le taux d'endettement de chaque individu. Ce taux correspond au pourcentage du revenu remboursé chaque mois par un 
individu. Vous arrondirez le résultat à 2 chiffres après la virgule :
"""
taux_endettement = round((prets['remboursement']) / (prets['revenu']) * 100, 2)
# print(taux_endettement)

"""
Pour éviter toute confusion, renommez la variable taux en taux_interet :
"""
prets.rename(columns={'taux': 'taux_interets'})

"""
Nous allons à présent créer deux dernières variables :

    cout_total correspondant au cout total du pret à partir du remboursement et de la duree
    benefices correspondant aux bénéfices mensuels réalisés par la banque sur le prêt

Nous simplifierons ici le calcul des bénéfices par :

bénéfices = (C∗T)/24

avec :

    C = cout total du prêt
    T = taux d'intérêt
"""
benefices = []
C = prets["remboursement"] + prets["duree"] * prets["taux"]

"""
A présent, nous souhaitons connaitre les 5 prêts sur lesquels nous produisons le plus de bénéfices. Mettez en place une solution pour les afficher :
"""
prets["benefices"] = C
print(prets.sort_values('benefices', ascending=False).head(5))


#############
# En résumé #
#############
"""
    On peut sélectionner une ou plusieurs colonnes d’un data frame via la syntaxe  mon_dataframe[col], où col est soit le nom de la colonne à sélectionner 
    (lorsqu’il n'y en a qu’une), soit une liste de noms de colonnes (lorsqu’il y en a plusieurs).

    Une colonne d’un data frame est une Series Pandas.

    De nombreuses manipulations sont possibles avec/via des Series ; on peut notamment :

        modifier, ajouter ou supprimer une colonne ;

        modifier le nom d’une colonne via la méthode.rename() ;

        changer le type d’une colonne via la méthode.astype() ;

        trier un data frame via la méthode.sort_values() .

Je vous propose à présent de voir comment filtrer les lignes pour avoir un contrôle total sur notre data frame.
"""