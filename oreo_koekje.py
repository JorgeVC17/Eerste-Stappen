# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:17:49 2023

@author: jorge
"""

oreo_koekje = ["Calorieën", 160 ,"Natrium (mg)", 190,"Koolhydraten (g)", 25,
                "Vet (g)", 7]
print("Een oreokoekje heeft", (oreo_koekje))

a = int(input("Hoeveel oreokoekjes heb je vandaag gegeten?"))

oreo_koekje2 =  [oreo_koekje[0], oreo_koekje[1] * a, oreo_koekje[2],
                 oreo_koekje[3] * a, oreo_koekje[4],oreo_koekje[5] * a,
                 oreo_koekje[6], oreo_koekje[7] * a,]

print("Je hebt vandaag", (oreo_koekje2), "gegeten")

if (oreo_koekje2[1] > 400):
    print("Stop! Je hebt meer dan 400 calorieën gegeten. Ik weet dat oreo's heel lekker zijn, maar stopt alsjeblieft!")