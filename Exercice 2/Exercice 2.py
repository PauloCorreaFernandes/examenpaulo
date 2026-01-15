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
        lbl_msg.setText("") #lbl = label
    except ValueError:
        lbl_msg.setText(" Erreur: Devez-vous tapez un nombre entier  !")

