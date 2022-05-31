# Créé par poret3, le 25/04/2022 en Python 3.7
from tkinter import *
import pyperclip as pc
from tkinter import messagebox


dict = [' ', "'", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
voyl = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

def crypto(mess,clé):   # Fonction qui permet de faire les changement sur le texte
    liste_mess = list(mess)
    mess_code = []
    for i in range (len(liste_mess)):   # Lance une boucle qui va changer les caractère 1 par 1
        mess_code.append(dict[(dict.index(str(liste_mess[i]))+int(clé))%(len(dict))])

    rep = "".join([str(elem) for elem in mess_code ])   #Lie les éléments pour retourner un texte
    return rep


def cripter(mess,clé):  # Fonction qui cripte un message avec une clé prédéfinie par l'utilisateur
    if test(mess) == True  :
        print(crypto(mess,clé))
        Rep.set(crypto(mess,clé))  # Change l'affichage sur l'interface pour affiche le nouveau message


def decripter(mess,clé):    # Fonction qui décripte un message avec une clé prédéfinie par l'utilisateur
    if test(mess) == True  :
        print(crypto(mess,-int(clé)))
        Rep.set(crypto(mess,-int(clé))) # Change l'affichage sur l'interface pour affiche le nouveau message


def chercher(mess):     # Fonction qui permet de retrouver un message cripter avec une clé inconnu
    mot_pert = []
    mot_tpert = []
    mot = []
    if test(mess) == True  :
        for i in range (len(dict)):     # On va décripter avec un nombre de clé infini
            cont = 0
            esp = 0
            mot_pot = crypto(mess,-i)   # On éffectu les changements avec une clé de valeur i
            liste_mot_pot = list(mot_pot)
            for k in range(len(liste_mot_pot)):
                try :                        # On fait des test pour classer les réponses de l'algorithme
                    voyl.index(liste_mot_pot[k])
                except ValueError as e :
                    cont = cont + 1
            if liste_mot_pot[k] == " " :
                esp += 1
            if cont <= ((len(liste_mot_pot)-esp)*0.70) :
                if cont <= ((len(liste_mot_pot)-esp)*0.60) :
                    mot_tpert.append(mot_pot)
                else :
                    mot_pert.append(mot_pot)
            else :
                mot.append(mot_pot)
        print(mot_tpert)
        print(mot_pert)
        Table(fenetre, mot_tpert, mot_pert) # On affiche un tableau avec les messages possible


def test(mess):     # Fonction qui nous permet de vérifier que notre base de donné a bien tout les caractères utilisés
    liste_mess = list(mess)
    test_rep = True
    for lettre in range(len(liste_mess)):
        try :
            dict.index(liste_mess[lettre])
        except ValueError as e :
            messagebox.showinfo("Erreur", ("Le caractère : { %s } n'est pas enregistré dans la base." %(liste_mess[lettre]))) # Crée une fenêtre qui affiche le caractère inconnu
            print("Le caractère :",liste_mess[lettre],"n'est pas enregistré dans la base.")
            test_rep = False
    return  test_rep


def copier(event):
    pc.copy(str(Rep.get()))     # Permet de copier un texte dans le presse papier


class Table:    # Crée une classe qui permet de faire un tableau

    def __init__(self,root,recher1, recher2):
        self.win = Toplevel(root)
        entry = Entry(self.win)
        entry.grid(column=0, row=0)
        entry.insert(END, 'Très pertinants')
        entry.config(state='readonly')
        entry = Entry(self.win)
        entry.grid(column=1, row=0)
        entry.insert(END, 'Pertinants')
        entry.config(state='readonly')
        for i in range(len(recher1)):
            entry = Entry(self.win)
            entry.grid(column=0, row=i+1)
            entry.insert(END, recher1[i])
            entry.config(state='readonly')
        for i in range(len(recher2)):
            entry = Entry(self.win)
            entry.grid(column=1, row=i+1)
            entry.insert(END, recher2[i])
            entry.config(state='readonly')


fenetre = Tk()    # Crée une fenêtre
fenetre.geometry("300x200")
fenetre['bg']='white'

label = Label(fenetre, text="Entrez la clé")    # Crée un label sur la fenêtre
label.pack()

s = Spinbox(fenetre, from_=0, to=10)    # Crée une barre d'entrée avec compteur
s.pack()

label = Label(fenetre, text="Entrez votre message")
label.pack()

value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str, width=30)     # Crée une barre avec entrée de texte
entree.pack()

Text=StringVar()
Text.set("L'algorithme trouve :")
texteLabel2 = Label(fenetre, textvariable = Text)
texteLabel2.pack()


Rep=StringVar()
Rep.set(" ")
texteLabel1 = Label(fenetre, textvariable = Rep)     # Crée un label pour afficher les résultats de l'algorithmes
texteLabel1.bind("<Double-Button-1>", copier)   # Paramètre le clic gauche pour lancer la fonction "copier"
texteLabel1.pack()


bouton=Button(fenetre, text="Cripter", command = lambda: cripter(str(entree.get()),s.get()))    # Crée un bouton pour lancer a fonction "cripter"
bouton.pack(side=LEFT, padx=20, pady=10)

bouton=Button(fenetre, text="Décripter", command = lambda: decripter(str(entree.get()),s.get()))
bouton.pack(side=LEFT, padx=20, pady=10)

bouton=Button(fenetre, text="Chercher", command = lambda: chercher(str(entree.get())))
bouton.pack(side=RIGHT, padx=20, pady=10)


fenetre.mainloop()  # Maintient la fenêtre ouverte
