# Créé par Mathys Poret, le 25/04/2022 en Python 3.7

dict = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
voyl = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

def crypto(mess,clé):
    liste_mess = list(mess)
    mess_code = []
    for i in range (len(liste_mess)):
        mess_code.append(dict[(dict.index(str(liste_mess[i]))+clé)%(len(dict))])

    rep = ''.join([str(elem) for elem in mess_code ])
    return rep


def cripter(mess,clé):
    if test(mess) == True  :
        print("Votre message cripter donne :", crypto(mess,clé))


def decripter(mess,clé):
    if test(mess) == True  :
        print("Votre message décripté donne :", crypto(mess,-clé))

def chercher(mess):
    mot_pert = []
    mot_tpert = []
    mot = []
    if test(mess) == True  :
        for i in range (len(dict)):
            cont = 0
            esp = 0
            mot_pot = crypto(mess,-i)
            liste_mot_pot = list(mot_pot)
            for k in range(len(liste_mot_pot)):
                try :
                    voyl.index(liste_mot_pot[k])
                except ValueError as e :
                    cont = cont + 1
            if liste_mot_pot[k] == ' ' :
                esp += 1
            if cont <= ((len(liste_mot_pot)-esp)*0.70) :
                if cont <= ((len(liste_mot_pot)-esp)*0.60) :
                    mot_tpert.append(mot_pot)
                else :
                    mot_pert.append(mot_pot)
            else :
                mot.append(mot_pot)
        print("les réponses les plus pértinantes sont :", mot_tpert)
        print("Nous avons aussi trouvé :", mot_pert)


def test(mess):
    liste_mess = list(mess)
    test_rep = True
    for lettre in range(len(liste_mess)):
        try :
            dict.index(liste_mess[lettre])
        except ValueError as e :
            print('Le caractère :',liste_mess[lettre],"n'est pas enregistré dans la base.")
            test_rep = False
    return  test_rep


