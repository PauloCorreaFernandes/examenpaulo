#Definition de la classe de base de personne
class Personne:
    def __init__(self, nom):
        #Attribu nom
        self.nom = nom

    def se_presenter(self):
        #Methode de presentation
        return " Je m'appelle " + self.nom

# Classe Etudiant qui herite de pesonne
class Etudiangt(Personne):
    def se_presenter(self):
        #Redefinnition de la methode  se presenter
        return " Je suis Etudiant et je m'appelle " + self.nom


# Classe Professeur qui herite de personne
class Professeur(Personne):
    def se_presenter(self):
        # Redefinition de la methode se presenter
        return " Je suis Professeur et je m'appelle " + self.nom

#Programme Principal
#Creation des objets
p1 = Etudiangt("Paulo")
p2 = Professeur("Barbari,Raouf")
p3 = Personne("Seye")

#Liste de contenant differents types d'objet
personnes = [p1, p2, p3]

#Boucle qui appelle la meme methode sur chaque objet
for p in personnes:
    print(p.se_presenter())



