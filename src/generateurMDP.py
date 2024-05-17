import random

class generateurMDP:

    NOM_DICTIONNAIRE = r"\dictionnaire.txt"

    def __init__(self,chemin):
        self.cheminDictionnaire = chemin + generateurMDP.NOM_DICTIONNAIRE
        self.listeMot = self.lireMDP()
        self.nbMDP = int(len(self.listeMot)) -1

    def lireMDP(self):
        listeMot = []
        with open(self.cheminDictionnaire, 'r') as file:
            for line in file:
                listeMot.append(line.strip())
        return listeMot

    def genererNombre(self,nbMax):
        return random.randint(0, nbMax)

    def genererListIndex (self):
        listeIndex = []
        listeMDP = []
        verif = True
        for i in range(6):
            random_number = self.genererNombre(nbMax=self.nbMDP)
            for index in listeIndex:
                verif = True
                if index == random_number:
                    i-=1
                    verif = False
              
            if verif == True:
                listeIndex.append(random_number)
                listeMDP.append(self.listeMot[random_number])

        return listeMDP
    
    def creerListe(self):
        listeIndex = self.genererListIndex()

        # for index in lis
        return listeIndex

    
