# Examen final : Exercice 1
#Programme que affiche deux triangles d'etoiles

class Triangle:
    def __init__(self,n):
    #constructeur : nombre de lignes
        self.n = n

    def triangle_gauche(self):
    #methode qui affiche le triangle de gauche
        symbol = '*'
        for i in range(self.n):
            print(symbol)
            symbole = symbole + '*'