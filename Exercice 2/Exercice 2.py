# programme que utilise le bibliotheque vu encalsse ...
import sys

#pip install PyQt6
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout, QLineEdit)

FICHIER = "resultats.txt"

def valider_operation():
    #Verifier que le champ N n'est pas vide
    if le_n.text().strip() == "":
        lbl_msg.setText(" Wrreur: le champ N est vide  !, S'il vous plait , tapez quelque nombre !")
        return
    try:
        n = int(le_n.text()) # peut lever ValueError
        resultat = n* 2
        le_double.setText(str(resultat)) #le= line edit
        lbl_msg.setText("") #lbl = label , effacer le message d'erreur si tout va bien
    except ValueError:
        lbl_msg.setText(" Erreur: Devez-vous tapez un nombre entier  !")

def sauvegarder_resultat():
    # Sauvegarde le double (champ resultat)
    if le_double.text().strip() == "":
        lbl_msg.setText(" Aucun resultat a sauvegarder !")
        return

    try:
        f = open (FICHIER, "w")
        f.write(le_double.text().strip()) #une seule ligne, une seule chiffre(ou nombre)
        f.close()
        lbl_msg.setText(" Resulta Sauvegarde sur resultats.txt")

    except Exception as e:
        print("Erreur du sauvegarder !", e)
        lbl_msg.setText("ERREUR : Impossible de sauvegarder !")

def charger_resultat():
    try:
        f = open(FICHIER, "r")
        contenu = f.read().strip()
        f.close()

        #validation simple : pas vide + entier
        if contenu == "":
            lbl_msg.setText("Erreur: fichier vide")
            return

        try:
            valeur = int(contenu)
            le_double.setText(str(valeur))
            lbl_msg.setText("Resultat charge depuis resultats.txt")
        except ValueError:
            lbl_msg.setText("Erreur: contenu du fichier invalide")

    except FileNotFoundError:
        lbl_msg.setText("Erreur: Resuktats.txt n'existe pas")
    except Exception as e:
        print("Erreur chargement :", e)
        lbl_msg.setText("Erreur: Impossible de charger !")

#1 - Creer un objet application
app = QApplication([])

#2 - Creer fenettre Widget
fen = QWidget()
fen.setWindowTitle("Exercice double")
fen.setGeometry(100,100,420,160)

# Layout
grid = QGridLayout()
fen.setLayout(grid)

#Labels + champs
lbl_nom = QLabel(("Entrer le valeur de N ")
le_n =  QLineEdit()

lbl_double = QLabel("Voici le double: ")
le_double = QLineEdit()
le_double.setReadonly(True)

#Boutons
btn_valider = QPushButton("Valider l'operation")
btn_valider.clicked.connect(valider_operation)

btn_sauve = QPushButton("Sauvegarder")
btn_sauve.clicked.connect(sauvegarder_resultat)

btn_load = QPushButton("Charger")
btn_load.clicked.connect(charger_resultat)

#Message (Petit Label d'erreur ou information)
lbl_msg = QLabel("")

#Placement
grid.addWidget(lbl_n, 0, 0)
grid.addWidget(le_n, 0, 1)

grid.addWidget(lbl_double, 1, 0)
grid.addWidget(le_double, 1, 1)

grid.addWidget(btn_valider, 2, 1)
grid.addWidget(btn_sauve, 2, 0)
grid.addWidget(btn_load, 3, 0)
grid.addWidget(lbl_msg, 3, 1)

#3 - Afficher
fen.show()

#4 - Executer
app.exec()





