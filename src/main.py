import random
import string
import sys
import os

module_location = r"C:\FLESTIM"
sys.path.append(module_location)

from data.data import data
from player.player import player
from generateurMDP import generateurMDP
from equipe import equipe,equipeAttaque,equipeVictime

NOMBRE_EQUIPE = 10

# Définition de la fonction main
def main():
    # path = module_location+"\nomenclature.xlsx"
    equipeBleu = equipeVictime("Bleu",NOMBRE_EQUIPE,"b","Victime")
    equipeRouge = equipeAttaque("Rouge",NOMBRE_EQUIPE,"r","Attaque")
    datastruct = data(module_location,NOMBRE_EQUIPE, equipeBleu, equipeRouge)
    docker_compose_content = generer_docker_compose(equipeBleu.getEquipe(), equipeRouge.getEquipe())
    dockerCompose = module_location + "\dockerCompose\docker-compose.yml"

    # Écrire le contenu dans un fichier docker-compose.yml
    with open(dockerCompose, 'w') as file:
        file.write(docker_compose_content)

    print("Le fichier docker-compose.yml a été généré avec succès.")

    attribuerVictime(equipeBleu,equipeRouge)
    afficherEquipe(equipeRouge)
    afficherEquipe(equipeBleu)
    
def genererBlocVM(joueur,lettreEquipe):
    blocVM = (
            f"  ubuntu_{lettreEquipe}-{joueur.numeroVM}:\n"
            f"    build:\n"
            f"      context: ../Ubuntu\n"
            f"      args:\n"
            f"        VM_HOSTNAME: {joueur.nomVM}\n"
            f"        VM_USERNAME: {joueur.user}\n"
            f"        VM_PASSWORD: {joueur.password}\n"
            f"    container_name: {lettreEquipe}{joueur.numeroVM}-{joueur.nomVM}\n"
            f"    hostname: {joueur.nomVM}\n"
            f"    ports:\n"
            f"      - '{joueur.port}:22'\n"
        )
    return blocVM

def generer_docker_compose(equipe_bleu, equipe_rouge):
    docker_compose = "version: '3.7'\nservices:\n"

    # Générer les services Ubuntu pour l'équipe Bleue
    for joueur in equipe_bleu:
        docker_compose += genererBlocVM(joueur,"b")

    # Générer les services Ubuntu pour l'équipe Rouge
    for joueur in equipe_rouge:
        docker_compose += genererBlocVM(joueur,"r")

    # Déclaration du réseau personnalisé "hack réseau"
    docker_compose += (
        "\nnetworks:\n"
        "  reseau:\n"
        "    driver: bridge\n"
    )
    return docker_compose

def attribuerVictime(equipeBleu,equipeRouge):
    generateur = generateurMDP(module_location)
    for index in range(NOMBRE_EQUIPE):
        # print(equipeRouge.getPlayer(index).afficher())
        equipeBleu.getPlayer(index).ajouterListeMDP(generateur.genererListIndex())
        # print(equipeBleu.getPlayer(index).afficher())

def afficherEquipe(equipe):
    for index in range(NOMBRE_EQUIPE):
        print(equipe.getPlayer(index).afficher())




# Vérification si le script est exécuté directement
if __name__ == "__main__":
    main()