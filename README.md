# Python microservice

Projet Health Calculator Microservice sur Python.

Ce projet consiste à développer un microservice en Python qui calcule des métriques de santé (IMC et TMB) via une API
REST. Le projet est conteneurisé avec Docker, géré avec un Makefile, et déployé sur Azure en utilisant GitHub Actions
pour le pipeline CI/CD.

## Sommaire

<!-- TOC -->

* [Fonctionnalités](#fonctionnalités)
* [Prérequis](#prérequis)
* [Installation et Configuration](#installation-et-configuration)
* [Structure du Projet](#structure-du-projet)
* [Déploiement sur Azure](#déploiement-sur-azure)

<!-- TOC -->

## Fonctionnalités

- **Calcul de l'IMC**
- **Calcul du TMB**

## Prérequis

- Python 3.12
- Docker
- Microsoft Azure

## Installation et Configuration

1. **Cloner le dépôt**

```bash
git clone git@github.com:Gautrot/python-microservice.git
cd python-microservice
```

2. **Configurations**

Ceci doit être fait après avoir installé `venv` dans le projet.

```bash
make init
```

3. **Execution des taches**

Cette commande lance le site en local. Vous pouvez changer les variables d'environnements dans un fichier `.env`. Le
fichier `.env.template` sert de repère des variables à utiliser pour le projet. Si vous êtes sous macOS, il est
nécessaire d'utiliser le port `5001`

```bash
make run
```

Par défaut, ce lien sera utilisé : http://localhost:5000.

Cette commande lance les tests unitaires. Il faut que le site soit ouvert pour lancer les tests.

```bash
make test
```

Cette commande lance la construction de l'image du projet sous Docker.

```bash
make build
```

## Structure du Projet

- app.py : Définit l'API Flask avec les endpoints `/bmi` et `/bmr`.
- classes : Les classes Python du projet.
    - person.py : Contient les fonctions utilitaires pour calculer l'IMC et le TMB.
- tests : Les tests unitaires.
    - test_health_calculator.py : Les tests unitaires pour valider l'API.
- templates : Les modèles HTML du projet.
- static : Les contenus statiques du projet (images, styles, etc.).
- Dockerfile : Conteneurise l'application.
- Makefile : Automatise les tâches.
- requirements.txt : Liste des dépendances Python du projet.
- ci-cd.yml : Workflow GitHub Actions pour le pipeline CI/CD.

## Déploiement sur Azure

1. **Créer un Resource Group**
    - Créez un nouveau Resource Group pour héberger le service de l'application.

2. **Créer un Azure App Service**
    - Créez un nouveau Web App dans Azure App Service pour héberger l'application.

3. **Configurer le profil de déploiement**
    - Ajoutez un secret dans les paramètres du dépôt GitHub nommé `AZURE_CREDENTIALS` et collez le contenu du secret
      comme ceci :

```json
{
  "clientId": "",
  "clientSecret": "",
  "subscriptionId": "",
  "tenantId": ""
}
```

4. **Déclencher le déploiement**
    - Poussez les modifications de code vers la branche principale pour déclencher le pipeline CI/CD et déployer sur
      Azure.
