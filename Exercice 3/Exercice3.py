#Examen Final : Exercice 3

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
