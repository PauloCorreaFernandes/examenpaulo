# Examen final : Exercice 1
#Programme que affiche deux triangles d'etoiles

class Triangle:
    def __init__(self,n):
    #constructeur : nombre de lignes
        self.n=n

    def triangle_gauche(self):
    #methode qui affiche le triangle a gauche
        symbol = "*"
        for i in range(self.n):
            print(symbol)
            symbol = symbol + "*"

    def triangle_droite(self):
    #methode  qui affiche le triangle a droite
        for i in range(1,self.n +1 ):
            print("*" * i)

class Affichage:
    def __init__(self,n):
        pass
    def afficher(self):
        #demander a usager le nombre de lignes
        n= int(input("Tapez le nombre de lignes que vous voulez :"))

        #creer un objet triangle
        t=Triangle(n)

        # afficher le premier triangle
        t.afficher_triangle_1()

        #laisser une ligne vide entre les deux triangles
        print()

        #afficher le deuxieme triangle
        t.afficher_triangle_2()


