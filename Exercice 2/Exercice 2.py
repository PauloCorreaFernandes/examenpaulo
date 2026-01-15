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

        except FileNotFoundError:
            lbl_msg.setText("Erreur: contenu du fichier invalide")
        except Exception as e:
            print("Erreur chargement :", e)
            lbl_msg.setText("Erreur: Impossible de charger !")

#1 - Creer un objet application
app = QApplication([])

#2 Creer fenettre Widget
fen = QWidget()
fen.setWindowTitle("Exercice double")
fen.setGeometry(100,100,420,160)

