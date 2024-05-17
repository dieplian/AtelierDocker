import random

class generateurMDP:

    NOM_DICTIONNAIRE = r"dictionnaire.txt"

    def __init__(self,nbMdpJoueur):
        self.listeDictionnaire = [] # Va contenir les mdp du fichier
        self.nbMdpJoueur = nbMdpJoueur # Nombre de mdp dans la liste du joueur
        self.lireDictionnaire()
        self.nbMDPTotal = int(len(self.listeDictionnaire)) -1 # Nombre de mdp dans le dictionnaire

    def lireDictionnaire(self):
        with open(generateurMDP.NOM_DICTIONNAIRE, 'r') as fichier:
            for ligne in fichier:
                self.listeDictionnaire.append(ligne.strip())


    def genererListeMotDePasse(self):
        lstPosition = []
        lstMotsDePasseJoueur = []
        verif = True

        for positionListe in range(self.nbMdpJoueur):
            random_number = random.randint(0,self.nbMDPTotal)

            for index in lstPosition:
                verif = True
                if index == random_number:
                    positionListe-=1
                    verif = False
                    break
              
            if verif == True:
                lstPosition.append(random_number)
                lstMotsDePasseJoueur.append(self.listeDictionnaire[random_number])

        return lstMotsDePasseJoueur