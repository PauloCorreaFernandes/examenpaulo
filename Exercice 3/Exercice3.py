#Examen Final : Exercice 3
from numpy.ma.core import minimum


#Programme qui demande 10 entiers et calcule
#le minimum , le maximum , la somme et la moyenne
#Les resultats sont conserves dans le fichier  resultats.txt

class Outils:
    def __init__(self):
        #liste pour stocker les entiers
        self.nombres = []

    def saisir(selfself):
        #demander 10 entiers au usager
        for i in range(1,11):
            n= int(input("Tapez un nombre entier(" + str(i) + "/10) : "))
            self.nombres.append(n)

    def min(self):
        #initialiser le minimum avec le premier nombre
        minimum = self.nombres[0]

        for n in self.nombres:
            if n < minimum:
                minimum = n

        return minimum

    def maximum(self):
        #calcule de la somme
        total = 0
        for n in self.nombres:
            total = total + n
        return total


