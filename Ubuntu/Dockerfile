# Utiliser une version spécifique d'Ubuntu comme base pour la prévisibilité
FROM ubuntu:20.04

# Éviter les messages interactifs pendant l'installation de paquets
ENV DEBIAN_FRONTEND=noninteractive

# Mettre à jour les paquets et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    openssh-server \
    sudo \
    curl \
    vim \
    iputils-ping \
    dumb-init \
 && rm -rf /var/lib/apt/lists/*

# Configurer le serveur SSH
# Créer le répertoire nécessaire pour le processus SSH
RUN mkdir /var/run/sshd \
    # Permettre l'accès SSH pour l'utilisateur root (Optionnel: à désactiver dans un environnement de production)
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    # Activer l'authentification par mot de passe
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    # Configurer SSH pour ne pas se déconnecter automatiquement
    && echo "ClientAliveInterval 120" >> /etc/ssh/sshd_config \
    && echo "ClientAliveCountMax 720" >> /etc/ssh/sshd_config


# Ajouter un utilisateur non-root pour SSH
RUN useradd -m -s /bin/bash -G sudo sshuser \
    && echo "sshuser:hector" | chpasswd \
    && echo "sshuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/sshuser

ARG VM_USERNAME="pomme"
ARG VM_PASSWORD="pomme"
# Ajouter un utilisateur non-root pour SSH
RUN useradd -m -s /bin/bash -G sudo $VM_USERNAME \
    && echo "$VM_USERNAME:$VM_PASSWORD" | chpasswd \
    && echo "$VM_USERNAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$VM_USERNAME

# Exposer le port SSH standard
EXPOSE 22
RUN mkdir /dictionnaire

COPY dictionnaire.txt /dictionnaire

# Utiliser dumb-init comme init system
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# Démarrer le serveur SSH en mode non-debug pour accepter les connexions
CMD ["/bin/sh", "-c", "while true; do /usr/sbin/sshd -D; done"]



