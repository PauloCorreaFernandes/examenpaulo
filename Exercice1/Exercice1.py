# Examen final : Exercice 1
#Programme que affiche deux triangles d'etoiles

class Triangle:
    def __init__(self,n):
    #constructeur : nombre de lignes
        self.n = n

    def triangle_gauche(self):
    #methode qui affiche le triangle a gauche
        symbol = '*'
        for i in range(self.n):
            print(symbol)
            symbol = symbol + '*'

    def triangle_droite(self):
    #methode  qui affiche le triangle a droite
        for in range(1, self.n + 1):
            print('*' * i)