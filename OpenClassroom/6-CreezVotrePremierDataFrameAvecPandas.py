# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857178-creez-votre-premier-data-frame-avec-pandas

##############################################
# Creez votre premier data frame avec Pandas #
##############################################
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857178-creez-votre-premier-data-frame-avec-pandas#/id/video_Player_1
import pandas as pd
pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)

#################################
# Preparez votre jeu de donnees #
#################################
"""
Comme nous avons pu le voir, les arrays NumPy sont particulièrement efficaces pour traiter des valeurs numériques. Mais les données, dans la réalité, ne sont pas composées 
uniquement de chiffres et de nombres.

En effet, on retrouve aussi :
    + des catégories ;
    + des labels ;
    + des dates ;
    + du texte brut.

De plus, ces données ont généralement un format prédéfini en analyse de données, où chaque ligne va correspondre à un individu (au sens statistique du terme), et chaque colonne va 
être une caractéristique spécifique des individus. C’est ce que l’on appelle une variable.

Le terme de variable lorsqu’on parle de données est à différencier d’une variable informatique ! Si la différence ne vous semble pas claire, je vous invite à relire le cours qui 
traite ce sujet.

Voici quelques exemples pour illustrer cela :
    + dans le milieu automobile, chaque individu sera une voiture, et on pourra avoir comme caractéristiques la puissance du moteur, les dimensions du véhicule, la marque, 
    le modèle, la couleur, etc. ;
    + dans une étude de grande distribution, chaque individu pourra être un produit sur lequel on aurait plusieurs informations (le prix, la catégorie, etc.) ;
    + dans le milieu bancaire enfin, chaque individu sera une personne, sur laquelle on aurait enregistré le salaire moyen, le genre, ses mensualités de remboursement de prêt, 
    etc. ;

Voilà par exemple à quoi pourrait ressembler ce dernier cas :
base de données au format Excel composé de 12 colonnes et de 6 lignes dont les entêtes comprennent 
identifiant, ville, code postal, revenu, remboursement, durée, type, taux, email, nom et genre
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857178-creez-votre-premier-data-frame-avec-pandas#/id/r-7862334


En explicitant le format des données, vous avez peut-être eu l’image d’un fichier Excel, et c’est une bonne idée ! Excel est encore pour beaucoup d’entreprises un format très 
utilisé pour stocker et déplacer des données. Mais ce n’est pas le seul, les données peuvent être stockées sous bien des formats différents.

Par exemple, on retrouve régulièrement des fichiers texte ou des fichiers CSV (pour comma-separated values). Ce sont simplement des fichiers contenant l’ensemble des données 
brutes, séparées par un délimiteur. 

Voici un exemple avec un jeu de données automobiles, dont le délimiteur est le point-virgule :
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857178-creez-votre-premier-data-frame-avec-pandas#/id/r-7862337

Cela peut également être sous la forme de fichier JSON. Le JavaScript Object Notation (JSON) est un format standard utilisé pour représenter des données structurées. 
Cela ressemble à un gros dictionnaire Python pouvant contenir lui-même d’autres dictionnaires et/ou listes. C’est une description un peu “réductrice”, mais une image vaut mieux 
que mille mots :
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857178-creez-votre-premier-data-frame-avec-pandas#/id/r-7862340

Nous n’aurons malheureusement pas l’occasion d'approfondir le format JSON dans le cadre de ce cours, mais il existe de nombreuses ressources qui traitent le sujet en détail. 
Le JSON est un format très standard dans le monde informatique !

Nous n’avons ici vu que les formats texte, JSON et CSV, mais la liste n’est naturellement pas exhaustive. De plus, plutôt que de stocker les données dans des fichiers, on a plutôt 
l’habitude de le faire dans des bases de données SQL. J’aborde le sujet très succinctement ici car il fera l’objet d’un autre cours !

Nous cherchons donc un outil qui nous permette de représenter les données avec le format souhaité (individus/variables), de manipuler différents types de données, et de lire les 
données provenant de différentes sources. Cet outil n’est autre que la librairie Pandas, et plus particulièrement les objets data frame. 

Le data frame est un objet Python permettant de représenter les données sous forme de tableau, où chaque colonne est explicitement nommée. Il reprend les mêmes paradigmes que 
l’array NumPy : chaque colonne peut naturellement être d’un type différent, mais une colonne ne peut contenir qu’un seul type ! Cette organisation simplifie l’accès aux variables, 
et permet de nombreuses manipulations de données plus ou moins complexes.

Mais du coup, quel est l’intérêt de la librairie NumPy si Pandas permet de faire tout cela ?

Excellente question ! Vous verrez au fur et à mesure de ce cours, et plus globalement de vos futures analyses de données, que vous serez régulièrement amené à jongler entre les 
deux. Il est assez courant que certaines méthodes appliquées à des data frames retournent des arrays, et qu’on ait besoin de retransformer ces arrays en data frames à postériori. 
C’est pourquoi il est nécessaire de maîtriser les deux librairies, pour être parfaitement armé avant de plonger dans une analyse de données.

En parlant de plonger, que diriez-vous de créer votre premier data frame ?

####################################
# Generez votre premier data frame #
####################################
Nous allons créer notre premier data frame à partir des formats cités ci-dessus ; et comme lorsqu’on aime, on ne compte pas… je vous propose d’importer le même jeu de données… 
sous 3 formats différents : format Excel, format CSV et format JSON.

Vous trouverez les trois fichiers dans ce dossier compressé. Passons à présent à la pratique :
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857178-creez-votre-premier-data-frame-avec-pandas#/id/video_Player_2

Il est important de placer les fichiers csv dans le même dossier que le notebook jupyter pour en faciliter l'importation !

Une fois le data frame importé, commence alors le travail principal d’un analyste de données : la manipulation de données. Et avant toute manipulation, il est nécessaire de 
connaître son jeu de données.

#######################################################
# Identifiez les caracteristiques de votre data frame #
#######################################################
Pandas met à disposition plusieurs méthodes pour pouvoir faire cela de façon efficace.
Aperçu du data frame

Comme présenté ci-dessus, un bon réflexe à adopter après l’importation, et après toute transformation importante, est de visualiser le jeu de données, ou du moins quelques lignes, 
afin de vérifier que tout s’est correctement déroulé.

Pour cela, il existe deux méthodes principales :
    + la méthode  .head()  permettant de sélectionner par défaut les 5 premières lignes du data frame. Il est possible de préciser entre parenthèses le nombre de lignes à 
    afficher ;
    + la méthode   .tail()  permettant de sélectionner par défaut les 5 dernières lignes du data frame. Il est également possible de préciser entre parenthèses le nombre de lignes 
    à afficher.
    
Il n’est pas possible (par défaut) d’afficher plus de 60 lignes d’un data frame, afin de ne pas surcharger inutilement le notebook. De façon plus globale, chercher à visualiser l’ensemble d’un data frame n’est généralement pas une bonne pratique. Si cela est tout à fait envisageable avec quelques dizaines de lignes, ça devient vite impossible avec plusieurs millions de lignes !
Si vous cherchez à afficher plus de 60 lignes, vous aurez finalement comme résultat les 5 premières et dernières lignes du data frame.

Voici quelques exemples :
"""


# Chargement du fichier
data = pd.read_csv("clients.csv")
print(data)
"""
https://www.youtube.com/watch?v=pz_0lRCrlNw&list=PLj6YeMhvp2S6gDMYrkDb81vneeuk_Lf3v&index=5
Quantité de mémoire utilisé par mon dataFrame
Si je ne veux pas charger toutes les colonnes car mon dataFrame est trop gros
"""
print(data.info(memory_usage='deep'))
data_2 = pd.read_csv("clients.csv", usecols=['email', 'nom'])
print(data_2)

# afficher les 5 premieres lignes
print(data.head())

# afficher les 2 dernieres lignes
print(data.tail(2))

# afficher les 5 premieres et dernieres lignes
print(data)

"""
On peut aussi accéder facilement aux caractéristiques globales d’un data frame.

###########################################
# Caractéristiques globales du data frame #
###########################################
Lorsqu’on parle de caractéristiques globales, il est question ici des attributs, des informations générales qu’on retrouve sur tous les data frames, et dont on aura besoin 
égulièrement.

En premier lieu viennent les dimensions d’un data frame. Combien de lignes comportent un data frame ? Et combien de colonnes ? Tout comme avec les arrays NumPy, il est possible de 
répondre à ces questions via l’attribut  .shape :
"""
print(data.shape)

"""
Le résultat sera un tuple. Sa lecture est relativement simple : le premier élément correspond au nombre de lignes, et le second au nombre de colonnes. On peut naturellement 
stocker le résultat de cet attribut dans une variable pour réutiliser ces éléments ultérieurement :
"""

# Caracteristiques globales du data frame
print(f"Caracteristiques globales du data frame data.shape data.shape[0] lignes x data.shape[1] colonnes: {data.shape} {data.shape[0]} lignes x {data.shape[1]} colonnes")
dim = data.shape
print(dim[0]) # 228
print(dim[1]) # 4

"""
Au-delà des dimensions, on peut avoir envie de connaître les types de chacune de nos variables. On peut accéder à cela très simplement à partir de l’attribut  .dtypes  :
"""
print(f"Connaitre les types d'un data frame data.dtypes: {data.dtypes}")
# En Pandas le type objet correspond en fait à une colonne de type chaine de caractere (ou string).


print(data.dtypes)
"""
Vous devriez avoir l’affichage suivant :
identifiant int64
email       object
nom         object
genre       object
dtype:      object

Vous noterez que le type de l’e-mail, du nom et du genre est objet, alors que nous avons pourtant des chaînes de caractères. C’est une chose à connaître, mais le type objet  de 
Pandas correspond en fait à une colonne de type chaîne de caractères (ou string ).

Bien qu’avec un affichage un peu austère, cela permet d’avoir facilement le type de chaque variable de notre data frame.

Enfin, nous avons évoqué précédemment le lien qui peut exister entre Pandas et NumPy. Je vous propose dès à présent de matérialiser ce lien en transformant notre data frame 
en array :
"""
clients_array = data.values
print(clients_array)

#############
# En resume #
#############
# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7857178-creez-votre-premier-data-frame-avec-pandas#/id/r-7857177
"""
    + En analyse de données, les données sont généralement représentées et manipulées sous un format de tableau, où chaque ligne représente un individu, et chaque colonne une 
    variable.

    + Le data frame de Pandas propose une implémentation de ce format en Python.

    + Les formats de stockage des données sont multiples : cela peut être via des fichiers délimités (CSV ou texte), ou encore des fichiers JSON ou Excel.

    + L’objet data frame de Pandas permet de manipuler simplement et efficacement les données :

        + en important très facilement tous ces différents formats ; 

        + en accédant facilement aux caractéristiques générales de notre jeu de données, comme les types de variables, le nombre de lignes, le nombre de colonnes, etc.
"""
