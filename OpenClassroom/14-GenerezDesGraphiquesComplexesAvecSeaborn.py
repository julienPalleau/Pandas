#################################################
# Générez des graphiques complexes avec Seaborn #
#################################################
"""
Matplotlib offre de nombreuses options pour personnaliser un graphique de A à Z ! Mais il est parfois laborieux de modifier des éléments spécifiques pour obtenir une belle
représentation. De plus, une petite modification peut très vite devenir plusieurs lignes de codes si on n'y prend pas garde.
"""
import matplotlib.pyplot as plt

####################################
# Identifiez quand utliser Seaborn #
####################################
"""
La librairie Seaborn vient proposer une alternative à Matplotlib. C'est également une librairie permettant de générer des graphiques, tout comme Matplotlib. J'irai même plus loin
en exprimant le fait que Seaborn est ce qu'on appelle une surcouche à Matplotlib.

Une sucouche correspond à... une couche située au-dessu d'une autre. C'est un terme qui est très régulièrement utilisé dans le monde de la téléphoinie mobile, avec les surcouches
Android. En gros, Android est la première couche disponible sur les Smartphones, et la surcouche du constructeur se rajoute par-dessus, offrant un nouveau design et de nouvelles
fonctionnalités.

Seaborn est exactement pareil vis-à-vis de Matplotlib. La Librairie reprend les mêmes principes que Matplotlib, mais en ajoutant quelque chose "par-dessus", afin d'offrir des
qualités de graphiques différents, des nouvelles fonctionnalités, etc. 
On pourrait imaginer que Seaborn est une voiture flambant neuve dont l'ensemble du châssis et le moteur seraient Matplotlib.

Et du coup, quelles sont ces nouvelles fonctionnalités offertes par Seaborn ?

Seaborn vient corriger plusieurs défaut de Matplotlib:
    + Il propose de multiples modèles graphiques de bonne qualité esthétique, en modifiant les options graphiques par défaut de Matplotlib ;
    + Il ajoute une interaction avec les data frames afin de faciliter grandement la génération de graphique à partir de ceux-ci ;
    + Il propose un catalogue - très - dense de fonctions graphiques pour répondre le plus précisément possible à une problématique donnée.
    
En contrepartie, Seaborn propose un peu moins d'options de personnalisation en tant que telles.

MAIS, comme Seaborn est juste une surcouche de Matplotlib, il est possible d'utiliser l'ensemble des options de personnalisatons vues dans le précédent chapitre, directement sur
les graphiques tracés avec Seaborn. Extraordinaire, non ?

Les deux librairies se complètent pour exploiter au mieux les avantages de l'une et de l'autre.
C'est un mariage particulièrement harmonieux.
"""

##########################
# Prenez en main Seaborn #
##########################
"""
Seaborn étant une surcouche de Matplotlib, il y a donc de nombreuses ressemblances entre les deux librairies.
Vous shouhaitez réliser un nuage de points ? Nous avions la fonction scatter avec Matplotlib, laissez moi vous présenter la fonction... scatterplot avec Seaborn.
Voilà comment l'utiliser:
"""
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)
prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets_final.csv')
prets.rename(columns={"taux": "taux_endettement"}, inplace=True)
sns.scatterplot(data=prets, x='revenu', y='taux_endettement')

"""
Explicitons un peu son fonctionnement:
    + dans un premier temps, on définit la data frame qui va être utilisé pour tracer le graphique, via l'argument data;
    + ensuite, il suffit de fixer les variables du data frame défini, à mettre en abscisse et en ordonnée.
    
Et le réel intérêt de Seaborn apparaît lorqu'on essaie d'ajouter des dimensions supplémentaires, comme des couleurs ou des tailles de points.
Reprenons le même graphique en ajoutant en couleur le type de graphique tracé. Là où on avait besoin d'une boucle avec Matplotlib, voilà le code avec Seaborn:
"""
# sns.scatterplot(data=prets, x='revenu', y='taux_endettement', hue='type')
# plt.show()
"""
... pour obtenir:
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858539-generez-des-graphiques-complexes-avec-seaborn#/id/r-7867564

En précisant la variable via l'argument hue, Seaborn crée automatiquement une couleur pour chaque valeur existante.
A présent, plutôt que l'information du type de prêt, on souhaite ajouter l'information de la durée du prêt. On peut faire cela en associant la taille d'un point à la durée
d'un prêt:
"""
# sns.scatterplot(data=prets, x='revenu', y='taux_endettement', size='duree')
# plt.show()

"""
Le nombre d'informations à afficher n'est pas limité, on pourrait très bien mixer la couleur avec la taille des points ! Cependant, attention à ne pas sacrifier la clareté et la
lisibilité d'un graphique en voulant y ajouter trop d'informatons.

Pour finaliser ce graphique, on peut utliser les différentses fonctions de Matplotlib vues précdémment:
"""
# plt.figure(figsize=(15, 6))
# # plt.rcParams.update({'font.size': 14})
#
# sns.scatterplot(data=prets, x='revenu', y='taux_endettement', hue='type')
# plt.ylabel("Taux d'endettement")
# plt.xlabel("Revenu mensuel (€)")
# plt.grid()
# plt.xlim(500, 7500)
# plt.legend(bbox_to_anchor=(1, 1.02))
# plt.title("Taux d'endettement en fonction du revenu mensuel\npar type de prêt contracté")
# plt.show()
"""
Explicitons les differentes fonctions utilisees:
    1.  La fonction rcParams.update, avec l'argument font.size, définit pour tous les graphiques - et non pas uniquement le graphique actuel - la taille de la police de tous les
        éléments (xlabel, title, legend, etc...) à 14.
    2.  grid permet d'afficher le quadrillage.
    3.  Via la fonction xlim, on fixe les limites des graduations de 500 à 7 500.
    4.  La fonction legend affiche la légende sur le graphique. La petite nouveauté ici est l'utilisation de l'argument bbox_to_anchor permettant de fixer la position de la légende
        en dehors du graphique, aux coordonnées renseignées.  
        
Agrégez des données avec Seaborn
Reprenons à présent le diagramme à barres du chiffre d'affaires par agence, réalisé précédemment. Avec Matplotlib, avant de tracer ce dernier, on avait eu besoin au préalable 
d'agréger nos données. La fonction barplot de Seaborn nous permet de réaliser cette étape directement à l'intérieur du graphique:
"""

# sns.barplot(data=prets, x='ville', y='remboursement', ci=None, estimator=sum)
# plt.show()

"""
Le début est similaire à ce que nous avions vu avec la fonction scatterplot, mais nous découvrons ici deux nouveaux arguments:
    +   ci, pour confidence interval (ou intervalle de confiance), qui ajoute les intervalles de confiance à chaque barre. Fixer cet argument à None permet de les faire disparaître
        ci is deprecated, use errorbar=None instead;
    +   estimator correspond à la fonction d'agrégation.
Tous les arguments vus précédemment fonctionnent également, notamment avoir des sous-groupes - par exemple : par type de prêt - en couleur:
"""
# import numpy as np
# # sns.barplot(data=prets, x='ville', y='remboursement', ci=None, estimator=np.mean, hue='type')
# sns.barplot(data=prets, x='ville', y='remboursement', errorbar=None, estimator=np.mean, hue='type')
# plt.show()

"""
Seaborn possède de nombreuses fonctions (plus d'une vingtaine) pour répondre à toutes les ituations possibles en termes de visualisation. Vous pouvez trouver la liste exhaustive 
sur la documentation officielle(https://seaborn.pydata.org/api.html). Mais pour en citer quelques-unes rapidement:
    +   lineplot pour tracer des courbes;
    +   boxplot pour des boîtes à moustaches;
    +   histplot pour des histogrammes;
    +   kdeplot pour un graphique à densité;
    +   pairplot pour tracer l'ensemble des variable numériques deux à deux, sur un seul graphique !

N'hésitez pas à tester toutes ces fonctions de votre côté pour apprécier la plus-value apportée par Seaborn.

Améliorez l'aspect graphique de vos visualisations
Seabon apporte un vrai plus esthétique par rapport à Matplotlib grâce aux palettes graphiques et aux thèmes.

Les palettes graphiques
Les palettes graphiques correspondent à un ensemble de couleurs qui vont être utilisées dans plusieurs palettes, utilisables à votre buise, qui sont particulièrement harmonieuse.

Pour fixer une nouvelle palette, on utilise la fonction set_palette de Seaborn. Donnons à notre graphique un aspect un peu plus pastel:
"""
import numpy as np
# sns.barplot(data=prets, x='ville', y='remboursement', ci=None, estimator=np.mean, hue='type')
sns.barplot(data=prets, x='ville', y='remboursement', errorbar=None, estimator=np.mean, hue='type')

### doesn't work ###
sns.set_theme(style='whitegrid', palette='pastel')
sns.color_palette("mako", as_cmap=True)
###

plt.show()


"""
Vous pourrez retrouver toutes les informations concernant les différentes palettes possibles, directement sur la page de couleurs correspondante 
(https://seaborn.pydata.org/tutorial/color_palettes.html?highlight=color).
"""

