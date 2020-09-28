#!/usr/bin/env python3
from cohen import ds
"""
Daten einlesen und visualisieren
================================

Die Exploration von Daten nimmt in der Regel viel Zeit in Anspruch und geschieht interaktiv, etwa in einem jupyter notebook. https://jupyter.org/

Hier demonstrieren wir nur einige wenige Ergebnisse, ohne die Exploration
im Detail durchzugehen.
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind, levene

# Excel-Sheet einlesen
scores = pd.read_excel('Minigolf.xlsx', sheet_name='Punkte')

print("Beschreibende Statistik")
print("=======================")
print(scores.describe())
print()

# Punkte pro Spieler summieren
player_scores = scores.sum()

# Besten Wert auswählen
winner = player_scores[player_scores == player_scores.min()]

# Schlechtesten Wert auswählen
loser = player_scores[player_scores == player_scores.max()]
print('Winner:', winner)
print('Loser:', loser)

# Persönliche Ergebnisse mit aufnehmen
people = pd.read_excel("Minigolf.xlsx", sheet_name="Personen")
people = people.set_index("Name")
people['Punkte'] = scores.sum()


print("Schließende Statistik I")
print("=======================")

# Gruppen am Merkmal "Geschlecht" aufsplitten.
# Hinweis: Der Datensatz basiert auf einer echten Runde Minigolf, bei der sich
# alle Personen selbst als M oder F identifizierten.
by_geschlecht = people.groupby('Geschlecht')

M = by_geschlecht.get_group("M").Punkte
F = by_geschlecht.get_group("F").Punkte

print()
print("Punkte nach Geschlecht")
print("----------------------")
print("Punkte M:", M)
print()
print("Punkte F:", F)
print()

# Test auf Gleichheit der Varianzen
_, p_levene = levene(M, F)
ALPHA = 0.05

# Mit Hilfe eines T-Tests stellen wir fest, wie hoch die Wahrscheinlichkeit
# ist, einen Mittelwertsunterschied dieser Größe gefunden zu haben
# obwohl in der Population kein Unterschied besteht.
#
# Mit anderen (nicht *ganz* richtigen) Worten: Ist der Unterschied zufällig?
result = ttest_ind(M, F, equal_var=(p_levene >= ALPHA))

print('Testergebnis: ')
print(result)
# Wenn das Ergebnis kleiner als 5% ist, also wir den Unterschied mit weniger
# als 5% Wahrscheinlichkeit gefunden haben, gehen wir von einem sicheren
# und nicht nur durch Zufall entstandenen Ergebnis aus
significance = (
    "Signifikant" if (result.pvalue < ALPHA / 2) else "Nicht Signifikant"
)
print(significance)
# Der Test ist nicht Signifikant. Es gibt in der Gruppe also offenbar keinen
# vom Zufall unterscheidbaren Leistungsunterschied beim Minigolf.

# Effekt visualisieren.
# Waren Personen mit Merkmal Geschlecht=M besser oder schlechter als Personen
# mit Geschlecht=F?
sns.boxplot(x="Geschlecht", y="Punkte", data=people)
plt.show()


print()
print("Schließende Statistik II")
print("========================")
# Um die Logik nochmal zu kontrollieren, betrachten wir
# einen eher offensichtlichen Effekt. Männer sind in der Regel
# etwas Größer als Frauen. Das zeichnet sich auch in der Stichprobe ab.

# Gruppen am Merkmal "Geschlecht" aufsplitten.
# Hinweis: Der Datensatz basiert auf einer echten Runde Minigolf, bei der sich
# alle Personen selbst als M oder F identifizierten.
by_geschlecht = people.groupby('Geschlecht')
M = by_geschlecht.get_group("M").Körpergröße
F = by_geschlecht.get_group("F").Körpergröße

# Test auf Gleichheit der Varianzen
_, p_levene = levene(M, F)
ALPHA = 0.05

result = ttest_ind(M, F, equal_var=(p_levene >= ALPHA))

print('Testergebnis: ')
print(result)
significance = (
    "Signifikant" if (result.pvalue < ALPHA / 2) else "Nicht Signifikant"
)
print(significance)
# Der Test ist Signifikant.

effect_size = ds(M, F)
print("Unterschied M:F in Standardabweichungen: ", effect_size)
# Der Effekt ist recht groß. So große Effekte sieht man oft schon
# "mit bloßem Auge".
# In der Psychologie freut man sich schon über Effekte zwischen 0.3 und 0.5

# Effekt visualisieren.
# Sind Personen mit Merkmal Geschlecht=M größer oder kleiner als Personen
# mit Geschlecht=F?
sns.boxplot(x="Geschlecht", y="Körpergröße", data=people)
plt.show()
