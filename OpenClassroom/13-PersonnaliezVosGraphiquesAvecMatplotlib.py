#https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858361-personnalisez-vos-graphiques-avec-matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#################################################
# Personnalisez vos graphiques avec Matplotlib #
################################################
"""
Nous avons justque-là tracé de nombreux graphiques fonctionnels. Cependant, ils ne sont pas vraiment conformes aux bonnes pratiques énonées précédemment.
En effet, sur la quasi-totalité, il manque des éléments indispensables pour faciliter la lecture comme le titre, les titres des axes ou la légende. Je vous propose de voir
maintenant comment ajouter tout cela avec Matplotlib.
"""

####################################
# Modifiez les éléments extérieurs #
####################################
"""
Dans un premier temps, concentrons-nous sur les aspects "extérieurs" d'un graphique. Si nous reprenons le graphique du chiffre d'affaire total réalisé par agence:
"""
# prets = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/prets_final.csv')
# plt.bar(height=prets['remboursement'], x=prets['ville'])
# plt.legend()
# plt.show()
# plt.close()
"""
Vous noterez qu'il manque quelques grilles de lecture:
    + On ne sait pas à quoi correspond l'axe des ordonnées, ni qu'elle est l'unité utilisée!
    + Il manque l'information globale de ce qui est représenté
    
Il nous faut donc ajouter un titre global et au moins le titre de l'un des axes. Pour ce faire, nous allons procéder de la même façon que précédemment: en appliquant des fonctions
supplémentaires à notre fenêtre graphique.
"""
# data = prets.groupby('ville')['remboursement'].sum()
# data = data.reset_index()
# print(data)
# plt.bar(data['ville'], data['remboursement'])
# plt.title("Chiffre d'affaire réalisé par agence", fontname='Arial', fontsize=18)
# plt.xlabel("Agences", color='red', fontweight='bold')
# plt.ylabel("Chiffre d'affaire (€)")
# plt.show()
# plt.close()

####################################
# Modifiez les éléments intérieurs #
####################################
"""
On a ainsi un graphique complet avec une grille de lecture claire. Il existe cependant d'autres options pour donner plus de clarté à une visualisation, ou pour la qualité
esthétique.

En effet, il y a de nombreux aspect internes au graphiques sur lesquels on peut jouer. Vous en avez déjà etraperçu un, avec l'affichage textuel des valeurs sur les pie plots ou les
barplots. 
Il est également possible de jouer - entre autres - sur les graduations (ou ticks, en anglais), le quadrillage, ou encore les couleurs de fond.
"""
# plt.figure()
# plt.bar(data['ville'], data['remboursement'])
# plt.title("Chiffre d'affaire réalisé par agence", fontsize=16)
# plt.ylabel("Chiffre d'affaire (€), fontsize=12")
# plt.show()
# plt.close()

#############
# Exercices #
#############
"""
Contexte
Les bénéfices mensuels par type de prêt pour lannée 2021 viennent de sortir au niveau de l'agence où vous travaillez. Dans le cadre du reporting mensuel, il vous est demandé de
réaliser un graphique spécifique représentant cette évolution, par type de prêt.

Consignes
Voici le graphique qui avait été obtenu l'an dernier:
https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science/7858361-personnalisez-vos-graphiques-avec-matplotlib#/id/r-7867559
On cherche à reproduire le même graphique avec les données de l'année 2021.
"""
CA = pd.read_csv('https://raw.githubusercontent.com/OpenClassrooms-Student-Center/fr-4452741-decouvrez-les-librairies-python-pour-la-data-science/main/data/CA.csv')
CA['date'] = pd.to_datetime(CA['date'])
print(CA)

plt.figure(figsize=(10, 7))
plt.plot(CA['date'], CA['immobilier'], label='immobilier', linewidth=3)
plt.plot(CA['date'], CA['automobile'], label='automobile', linewidth=3)
plt.plot(CA['date'], CA['consommation'], label='consommation', linewidth=3)
plt.legend(loc='upper right')
plt.ylabel('Bénéfice net (€)', fontsize=13)
plt.yticks(fontsize=11)
plt.title("Bénéfices mensuels nets sur l'année 2020, par type de prêt", fontsize=14)
plt.grid(color='gray', linestyle='-', linewidth=0.5)
plt.show()

