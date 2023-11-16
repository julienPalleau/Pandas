# https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858285-tracez-des-graphiques-avec-matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#########################################
# Tracez des graphiques avec Matplotlib #
#########################################

########################
# Decouvrez Matplotlib #
########################
"""
A ce stade, nous avons réuni de nombreuses informations sur nos clients, que nous pourrions mixer et repésenter au sein de différents graphiques.

Par exemple, plutôt que d'avoir l'information sous forme de tableau, il serait intéressant de représenter le chiffre d'affaires total par agence.
On peut aussi regarder le taux d'endettement de nos clients en fonction de leur revenu, pour voir si une tendance se dégage.

Il nous faut donc une librairie pour réaliser ces différents graphiques avec Python. Il en existe une multitude, et c'est parfois un peu compliqué de comprendre l'intérêt et la
plus-value de l'une par rapport à une autre. C'est pourquoi je vous propose de regarder en détail la librairie principalement utlisée pour réaliser des visualisations. Matplotlib.
Enfin, nous allons plutôt utiliser pyplot qui est inclus dans Matplotlib.
Voilà comment importer cette dernière:
import matplotlib.pyplot as plt

Si dans votre vie vous avez été amené à réaliser des calculs scientifques, ce nom vous dit peut être quelque chose. C'est normal! Car la façon de créer des graphiques avec
Matplotlib est calquée sur celle d'un autre langage très utlisé en calcul scientifque MATLAB. Si vous avez dejà utlisé ce dernier, vous allez retrouver de grandes similitudes.

Chaque représentation graphique a une fonction correspondante avec Matplotlib:
    + nuage de points ou scatter plot, en anglais: scatter();
    + digrammes en ligne ou en courbes: plot();
    + histogrammes: hist();
    + diagrammes circulaires: pie().
    
Que diriez-vous de découvrir une application concrète de ces fonctions ? C'est parti !
"""

##################################
# Tracez vos premiers graphiques #
##################################
"""
Le nuage de points
Cherchons à représenter un des graphiques cités ci-dessus: représenter le taux d'endettement en fonction du revenu. Ces deux variables on numériques, sans évolution dans le temps:
nous allons donc tracer un nuage de points, via la fonction scatter. Cette fonction nécessite de définir x et y, qui sont les valeurs à placer en abscisse et en ordonnée.
"""
pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows', 1000)
prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets.csv')
prets.rename(columns={'taux': "taux_endettement"}, inplace=True)

# plt.scatter(prets['revenu'], prets['taux_endettement'])
# plt.show()
# plt.close()

"""
Il existe de nombreuses options pour personnaliser un nuage de points. On peut modifier:
    + La couleur des points, en utlisant l'argument color ou c;
    + La taille des points, via l'argument size ou s;
    + le type de marqueur via l'argument marker;
    + la transparence des points via l'argument alpha.
    
Liste complete des options: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html
"""
# plt.scatter(prets['revenu'], prets['taux_endettement'],
#             s=60, alpha=0.5, c='red', marker='P')
# plt.show()
# plt.close()
"""
Cette liste n'est qu'une infime partie de ce que vous pouvez modifier... Vous trouverez la liste complète des arguments sur la documentation officielle de la
fonction (https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html).

On souhaite maintenant représenter le chiffre d'affaire total par agence. Comme nous l'avons vu précédemment, il existe deux possibilités pour cela : soit un diagramme à barres,
soit un diagramme circulaire. Nous allons réaliser ces deux visualisations.
"""
###########################
# Le Diagramme circulaire #
###########################
"""
Son utilisation est très similare à celle de scatter. I y a deux arguments à préciser: labels, correspondant à la variable non numérique, celle sur laquelle ont été agrégées les
données, et x, les valeurs agrégées correspondantes.
La première étape va donc être d'aggréger les données:
"""
data = prets.groupby('ville')['remboursement'].sum()
data = data.reset_index()

"""
Traçons à présent notre camembert à partir de ces données agrégées:
"""
# plt.pie(x=data['remboursement'], labels=data['ville'])
# plt.show()
# plt.close()

"""
On peut également améliorer ce graphique en affichant textuellement le pourcentage associé à chaque "part". Pour cela, il faut spécifier un format numérique via l'argument autopct
Par exemple:
"""
# plt.pie(x=data['remboursement'], labels=data['ville'], autopct='%.2f%%')
# plt.show()
# plt.close()

"""
Explicitons rapidement ce format: il permet d'afficher la part du chiffre d'affaires total réalisé par chaque agence, avec 2 chiffres après la virgule, et suivie du caratère %.

Vous pourrez trouver les arguments possibles de la fonction pie sur la documentation officielle(https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html)
"""

#########################
# Le diagramme à barre #
########################
"""
L'alternative au diagramme circulaire est un diagramm à barres ! On peut représenter exactement la même information, mais avec une perspective différente.
Pour utiliser la fonction bar, qui est l'implémentation de Matplotlib des diagrammes à barres, il faut préciser deux arguments:
    + x: les fifférentes valeurs de la variable non numérique, l'équivalent du labels de pie;
    + height: les valeurs agrégées, équivalent du x de pie.
Représentons maintenant la même information - le chiffre d'affaires total par agence - via un diagramme à barres:
"""
# plt.bar(height=data['remboursement'], x=data['ville'])
# plt.show()
# plt.close()
"""
Et si vous shouhaitez ordonner du plus grand au plus petit ? Il faudra tricher un petit peu.
En effet, la fonction bar de Matplotlib ne permet pas, par défaut, de réaliser cela...
MAIS on peut tout de même trier le data frame en amont.
"""
# data_sorted = data.sort_values('remboursement', ascending=True)
# plt.bar(height=data_sorted['remboursement'], x=data_sorted['ville'])
# plt.show()
# plt.close()

"""
Documentation: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.bar.html
"""

#################
# L'histogramme #
#################
"""
Lorsqu'il s'agit de connaissance client dans le milieu bancarire, on arrive assez rapidement à la question: Comment se répartissent nos clients en termes de revenus ?
A-t-on majoritairemnet des classes moyennes ? ou des revenus plus modestes ?
L'histogramme est particulièrement utile lorsqu'on souhaite avoir une idée de la distribution d'une variable, et donc particulièrement adéquat pour répondre à cette problématique.
La fonction Matplotlib correspondate est hist. Il suffit de lui passer en paramètre la variable numérique dont on souhaite connaître la distribution:
"""
# plt.hist(prets['revenu'])
# plt.show()
# plt.close()
"""
En un coup d'oeil, on peut déterminer, grâce à l'historgramme, que nous avons majoritairement des revenus modestes au sein de notre clientèle.
Il existe de nombreuses possibilité de personnalisation, notamment sur le nombre de tranches, leur composition, etc. Vous pourrez retrouver tout cela, une fois de plus, dans la
documentation de la fonction.(https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.hist.html)
"""

################
# Les courbes #
###############
"""
On souhaite suivre l'évolution du chiffre d'affaire sur les 4 premiers mois, pour voir la façon dont il varie, éventuellement anticiper la suite.
Nous avons pour cela à notre disposition le chiffre d'affaires réalisé par notre banque sur les prêts de janvier à avril 2013:
"""
# evolution_ca = pd.DataFrame({'date': ['2013-01-01', '2013-02-01', '2013-03-01', '2013-04-01'], "chiffre d'affaire": [183000, 193020, 179032, 219174]})
# print(evolution_ca)

"""
On a ici une évolution dans le temps, donc le choix de représentation le plus pertinent serait de tracer une courbe.
Pour ce faire, on utilise la fonction plot de Matplotlib. Celle-ci prend deux arguments en entrée: les informations à mettre en abscisse, et celles à mettre en ordonnées. Voilà
comment tracer l'évolution de notre chiffre d'affaires:
"""
# plt.plot(evolution_ca['date'], evolution_ca["chiffre d'affaire"])
# plt.show()
# plt.close()

"""
Nous avons eu un chiffre d'affaires en hausse globale sur le premier tiers de 2013:

Comme pour le nuage de points, il existe de très nombreuses options de personnalisation. Vous pouvez jouer sur la couleur de la ligne (color ou c), son style (linestyle ou ls), son
épaisseur (linwidth ou lw), si on shouhaite ajouter un marqueur en plus de la ligne (marker), etc. Vous trouverez l'ensemble des possibilités sur la 
documentation(https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.plot.html)

Voici par exemple le même graphique, avec des lignes rouges hachrées, où on ajoute un point à chaque date:
"""
# plt.plot(evolution_ca['date'], evolution_ca["chiffre d'affaire"], marker='o', linestyle='--', color='red')
# plt.show()
# plt.close()

"""
Ca donne un autre style à notre graphique:
Ces différents graphiques sont sympas, mais ils ne respectent pas vraiment les bonnes pratiques présentées précédemment...
C'est un excellent point ! En effet, il manque pas mal d'informations sur l'ensemble de ces graphiques... mais ne vous inquiétez pas, ce n'est pas un oubli de ma part, nous aurons
l'occasion de voir comment corriger tout cela dans le prochain chapitre.
"""

###################################################
# Créez plusieurs graphiques sur une même fenêtre #
###################################################
"""
Nous avons 6 agences différentes avec plusieurs dizaines de clients par agence. Le responsable national shouaite avoir, en un seul graphique, une idée du comportement des agences
en termes d'attribution de taux, en fonction du revenu.

Représenter le revenu en fonction du taux est assez simple: on peut faire cela via un nuage de points. Mais comment représenter, en plus, l'informationd de l'agence?

En ajoutant une information supplémentaire à notre graphique, comme la couleur des points !

Cependant, il n'existe pas d'option par défaut avec Matplotlib pour mettre en couleur les points.
On va être forcés de créer plusieurs graphiques - un par agence - qu'on va superposer sur une seule même fenêtre graphique.
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858285-tracez-des-graphiques-avec-matplotlib#/id/video_Player_1
"""
# df1 = prets.loc[prets['ville'] == 'TOULOUSE', :]
# df2 = prets.loc[prets['ville'] == 'PARIS', :]
#
# plt.scatter(df1['revenu'], df1['taux_endettement'], label='TOULOUSE')
# plt.scatter(df2['revenu'], df2['taux_endettement'], label='PARIS')
# plt.legend()
# plt.show()
#
# for ville in prets['ville'].unique():
#     df = prets.loc[prets['ville'] == ville, :]
#     plt.scatter(df['revenu'], df['taux_endettement'], label=ville)
# plt.legend()
# plt.show()

############
# Exercice #
############
"""
Contexte:
Vous êtes en train de préparer le reporting à présenter chaque fin de mois à votre responsable.
La présentation devra comprendre certains graphiques clés: vous allez donc devoir utiliser vos compétences en data visualisaton pour produire les différentes visualisations
attendues.

Consignes:
Les graphiques à produire sont donc:
    + la propotion de chaque type de prêt;
    + Le bénéfice mensuel réalisé en fonction du revenu du client pour les prêts immobiliers;
    + la distribution des bénéfices réalisés;
    + Le bénéfice mensuel total réalisé par agence.
"""


##############
# En résumé #
#############
"""
+ Matplotlib met à disposition une fonction par type de graphique souhaité:
    + plot: pour les courbes;
    + bar: pour les diagrammes à barres;
    + pie: pour les diagrammes circulaires;
    + hist: pour faire des histogrammes;
    + scatter: pour les nuages de points.
    
+ Personalisez vos différents graphiques en utilisant les différents paramètres de chaque fonction.
+ Tracez différents graphiques sur une seule fenêtre graphique, pour ajouter des dimensions supplémentaires.
"""
############################################
# 1 - proportion de prêt par type de prêt. #
############################################
prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets_final.csv')
print(prets)
# On peut avec groupby:
type_agreg = prets.groupby('type').size().reset_index()

# via la fonction value_counts:
type_agreg = prets['type'].value_counts().reset_index()

# renomer toutes les colonnes en une fois:
type_agreg.columns = ['type', 'nombre']

print(type_agreg)

"""
Pour la visualisation, vous pouvez opter pour un diagramme à barres ou un diagramme circulaire :
"""
# diagramme à barres
plt.bar(type_agreg['type'], type_agreg['nombre'])
plt.show()
plt.close()

# diagramme circulaire
plt.pie(x=type_agreg['nombre'], labels=type_agreg['type'], autopct='%.2f%%')
plt.show()
plt.close()

##################################################################################
# 2 - bénéfice mensuel réalisé en fonction du revenu client - prêts immobiliers. #
##################################################################################
"""
On shouaite représenter 2 variables numériques: on optera donc pour un nuage de points
"""
prets_imo = prets.loc[prets['type'] == 'immobilier', :]
plt.scatter(prets_imo['revenu'], prets_imo['benefices'])
plt.show()
plt.close()

##############################################
# 3 - La distribution des bénéfices réalisés #
##############################################
"""
On souhaite représenter la distribution d'une variable numérique: on utilisera donc un histogramme.
"""
plt.hist(prets['benefices'])
plt.show()
plt.close()

#################################################
# 4 - Bénéfice mensuel total réalisé par agence #
#################################################
benef_ville = prets.groupby('ville')['benefices'].sum().reset_index()
plt.bar(benef_ville['ville'], benef_ville['benefices'])
plt.show()
plt.close()

