import random
import string
import sys
import os

chemin_module = r"C:\Projets\AtelierDocker"
chemin_dockerCompose = chemin_module + "\dockerCompose\docker-compose.yml"

# sys.path.append(chemin_module)

from informations.traitement import traitementDonnee
from player.player import player
from generateurMDP import generateurMDP
from equipe import equipe,equipeAttaque,equipeVictime

NOMBRE_EQUIPE = 10
NOMBRE_MDP = 6

# Définition de la fonction main
def main():
    equipeBleu = equipeVictime("Bleu",NOMBRE_EQUIPE,"b","Victime")
    equipeRouge = equipeAttaque("Rouge",NOMBRE_EQUIPE,"r","Attaque")

    traitementDonnee(chemin_module,NOMBRE_EQUIPE, equipeBleu, equipeRouge)

    ecrireFichierDockerCompose(equipeBleu,equipeRouge)

    attribuerVictime(equipeBleu,equipeRouge)

    afficherEquipe(equipeRouge)
    afficherEquipe(equipeBleu)
    
def ecrireFichierDockerCompose(equipeBleu,equipeRouge):
    docker_compose_content = generer_docker_compose(equipeBleu.getEquipe(), equipeRouge.getEquipe())

    with open(chemin_dockerCompose, 'w') as file:
        file.write(docker_compose_content)

    print("Le fichier docker-compose.yml a été généré avec succès.")


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
    generateur = generateurMDP(NOMBRE_MDP)
    for index in range(NOMBRE_EQUIPE):
        equipeBleu.getPlayer(index).ajouterListeMDP(generateur.genererListeMotDePasse())

def afficherEquipe(equipe):
    for index in range(NOMBRE_EQUIPE):
        print(equipe.getPlayer(index).afficher())



# Vérification si le script est exécuté directement
if __name__ == "__main__":
    main()