#Definition de la classe de base de personne

class Personne:
    def __init__(self, nom):
        #Attribu nom
        self.nom = nom

    def se_presenter(self):
        #Methode de presentation
        return " Je m'appelle " + self.nom




