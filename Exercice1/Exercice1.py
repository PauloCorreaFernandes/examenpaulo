# Examen final : Exercice 1
#Programme que affiche deux triangles d'etoiles

class Triangle:
    def __init__(self,n):
    #constructeur : nombre de lignes
        self.n=n

    def afficher_deux_triangles(self):
        #afficher deux triangles cote a cote
        for i in range(1, self.n + 1):
            gauche= "*" * i
            espaces= " " * (2 *(self.n - i) +2)
            droite= "*" * i
            print(gauche + espaces + droite)

class Affichage:
    def __init__(self):
        pass

    def afficher(self):
        #demander a usager le nombre de lignes
        n= int(input("Tapez le nombre de lignes que vous voulez :"))

        #creer un objet triangle
        t=Triangle(n)
        t.afficher_deux_triangles()

# programme principal
a = Affichage()
a.afficher()


