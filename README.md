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

Cette tâche doit être lancée après avoir installé `venv` dans le projet.

```bash
make init
```

3. **Execution des tâches**

Cette commande lance le site en local avec `flask`. Vous pouvez changer les variables d'environnements dans un fichier
`.env`. Le fichier `.env.template` sert de repère des variables à utiliser pour le projet. Si vous êtes sous macOS, il
est nécessaire d'utiliser le port `5001`. Ce lien sera utilisé par défault une fois que la tâche est
lancée : http://localhost:5000.

```bash
make run
```

Cette commande lance les tests unitaires avec `pytest`. Il faut que le site soit ouvert pour lancer les tests.

```bash
make test
```

Cette commande lance la construction de l'image du projet sous Docker.

```bash
make build
```

## Structure du Projet

- app.py : Définit l'API Flask avec les endpoints `/bmi` et `/bmr`.
- classes : Les classes du projet sous Python.
    - person.py : Contient les fonctions utilitaires pour calculer l'IMC et le TMB.
- tests : Les tests unitaires.
    - test_health_calculator.py : Les tests unitaires pour valider l'API.
- templates : Les modèles HTML du projet.
- static : Les contenus statiques du projet (images, styles, etc.).
- Dockerfile : Conteneurise l'application.
- Makefile : Automatise les tâches.
- requirements.txt : Liste des dépendances Python du projet.
- main_healthapp-python.yml : Workflow GitHub Actions pour le pipeline CI/CD.

## Déploiement sur Azure

1. **Créer un Resource Group**

Créez un nouveau Resource Group pour héberger le service de l'application ayant comme nom "healthapp-python".

2. **Créer un Azure App Service**

Créez un nouveau Web App dans Azure App Service pour héberger l'application ayant comme nom "healthapp-python".

3. **Configurer le profil de déploiement**

Ajoutez un secret dans les paramètres du dépôt GitHub nommé `AZURE_CREDENTIALS` et collez le contenu du secret comme
ceci :

```json
{
  "clientId": "",
  "clientSecret": "",
  "subscriptionId": "",
  "tenantId": ""
}
```

Pour obtenir leurs valeurs, il faut faire ces actions suivantes :

- `clientSecret`, `clientId` et `tenantId` :
    - Allez dans Microsoft Entra ID > App registrations, puis allez sur votre application.
    - Copiez les valeurs "Application (client) ID" et "Directory (tenant) ID" dans `clientId` et `tenantId`
      respectivement.
    - Dans l'application, allez sur Certificates & secrets et créez une clé.
    - Copiez la valeur depuis la colonne "Value" et collez la pour `clientSecret`.
- `subscriptionId` :
    - Allez dans Subscriptions, puis copiez la valeur depuis la colonne "Subscription ID" dans `subscriptionId`

4. **Déclencher le déploiement**

Poussez les modifications de code vers la branche principale (`main`) pour déclencher le pipeline CI/CD et déployer sur
Azure.
