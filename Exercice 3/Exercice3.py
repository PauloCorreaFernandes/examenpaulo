#Examen Final : Exercice 3
from numpy.ma.core import minimum


#Programme qui demande 10 entiers et calcule
#le minimum , le maximum , la somme et la moyenne
#Les resultats sont conserves dans le fichier  resultats.txt

from numpy.ma.core import minimum
class Outils:
    def __init__(self):
        #liste pour stocker les entiers
        self.nombres = []

    def saisir(self):
        #demander 10 entiers au usager
        for i in range(1, 11):
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

    def moyenne(self):
        #calcul de la moyenne
        return self.somme() / len(self.nombres)

#programme principal
o = Outils()
o.saisir()

min_val = o.min()
max_val = o.max()
somme_val = o.somme()
moyenne_val = o.moyenne()

print("Minimum : " , min_val())
print("Maximum : " , max_val())
print("Somme : " , somme_val())
print("Moyenne : " , moyenne_val())

#Sauvegarder les resultats dans le fichier  resultat.txt
fichier = open("resultats.txt", "w")
fichier.write("Resultats de lexercice 3\n")
fichier.write("Minimum : " + str(min_val)+"\n")
fichier.write("Maximum : " + str(max_val)+"\n")
fichier.write("Somme : " + str(somme_val)+"\n")
fichier.write("Moyenne : " + str(moyenne_val)+"\n")
fichier.close()






