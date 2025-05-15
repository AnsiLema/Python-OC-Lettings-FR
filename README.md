# OC Lettings Site

Application Django développée pour le site web d'Orange County Lettings.  
Il s'agit d'une plateforme de locations de vacances, avec gestion des profils utilisateurs et des annonces de logements.

- 🔒 Sécurité et journalisation (Sentry)
- ✅ Qualité de code et tests automatisés
- 🐳 Conteneurisation Docker
- ⚙️ Déploiement via GitLab CI/CD + Render

---

## 🔧 Technologies utilisées

- **Python 3.12**
- **Django 5.2**
- **Gunicorn** (serveur WSGI)
- **Whitenoise** (servir les fichiers statiques)
- **pytest + coverage** (tests)
- **flake8** (linting)
- **Docker** (image slim)
- **Render** (hébergement)
- **GitLab CI/CD** (pipeline automatisé)

---


## Table des Matières

1.  [Description du Projet](#description-du-projet)
2.  [Objectifs des Améliorations Récentes](#objectifs-des-améliorations-récentes)
3.  [Technologies Utilisées](#technologies-utilisées)
4.  [Prérequis](#prérequis)
5.  [Installation](#installation)
    *   [Clonage du Dépôt](#clonage-du-dépôt)
    *   [Environnement Virtuel](#environnement-virtuel)
    *   [Dépendances](#dépendances)
    *   [Configuration de l'Environnement](#configuration-de-lenvironnement)
6.  [Démarrage Rapide (Lancement Local)](#démarrage-rapide-lancement-local)
7.  [Tests et Qualité du Code](#tests-et-qualité-du-code)
8.  [Surveillance et Gestion des Erreurs (Sentry)](#surveillance-et-gestion-des-erreurs-sentry)
    *   [Configuration de Sentry](#configuration-de-sentry)
    *   [Stratégie de Logging dans l'Application](#stratégie-de-logging-dans-lapplication)
    *   [Middleware de Surveillance (`monitoring/monitoring_middleware.py`)](#middleware-de-surveillance-monitoringmonitoring_middlewarepy)
    *   [Ce que Sentry Capture](#ce-que-sentry-capture)
9.  [Utilisation avec Docker](#utilisation-avec-docker)
10. [Déploiement et Pipeline CI/CD](#déploiement-et-pipeline-cicd)
    *   [Aperçu du Pipeline (GitLab CI/CD & Render)](#aperçu-du-pipeline-gitlab-cicd--render)
    *   [Configuration Requise pour le Déploiement](#configuration-requise-pour-le-déploiement)
    *   [Processus de Déploiement (via la branche `master`)](#processus-de-déploiement-via-la-branche-master)

---

## 1. Description du Projet

OC Lettings Site est une application web de gestion de locations immobilières. Ce projet a récemment fait l'objet
d'une refactorisation majeure visant à améliorer son architecture, sa maintenabilité et sa robustesse.

## 2. Objectifs des Améliorations Récentes

Le projet a été modernisé pour répondre aux standards actuels de développement web, notamment par :

1.  **Amélioration de l’architecture modulaire :**
    *   Réorganisation du code en applications distinctes : `lettings` et `profiles`.
    *   Migration des modèles (`Address`, `Letting`, `Profile`) et des données existantes vers ces nouvelles applications.
    *   Déplacement des templates HTML dans des dossiers spécifiques à chaque application.
    *   Réorganisation des URLs avec des espaces de noms.
    *   Renommage des vues et templates d'index (`lettings_index` -> `index`, `profiles_index` -> `index`).
    *   Suppression des fichiers inutiles dans l'application `oc_lettings_site` originelle.
2.  **Résolution de problèmes :**
    *   Correction des erreurs de linting (conformité `flake8` sans modifier `setup.cfg`).
    *   Correction de la pluralisation du terme "adresse" dans l'interface d'administration.
    *   Mise en place de pages d'erreur personnalisées (404, 500).
    *   Ajout de docstrings claires pour les modules, classes et fonctions.
    *   Mise en place de tests unitaires et d'intégration (vues, URLs, modèles) avec une couverture supérieure à 80%.
3.  **Surveillance et suivi des erreurs avec Sentry :**
    *   Intégration de Sentry pour la surveillance des erreurs en production.
    *   Configuration du module `logging` de Python pour envoyer des informations pertinentes à Sentry et/ou en console.
4.  **Mise en place d'un pipeline CI/CD :**
    *   Automatisation des tests, du linting et de la vérification de la couverture.
    *   Conteneurisation de l'application avec Docker et publication sur Docker Hub.
    *   Déploiement automatisé sur un hébergeur PaaS (ex: Render).

L'objectif principal de cette refactorisation était d'améliorer la structure interne sans altérer l'apparence ou les fonctionnalités du site, y compris la section d'administration.

## 3. Technologies Utilisées

*   **Langage :** Python 3.12
*   **Framework Web :** Django 5.2
*   **Serveur d'application WSGI :** Gunicorn
*   **Whitenoise** (servir les fichiers statiques)
*   **Gestion des dépendances :** pip, `requirements.txt`
*   **Base de données (par défaut en développement) :** SQLite
*   **Tests :** Pytest, pytest-django, Coverage.py
*   **Linting :** Flake8
*   **Surveillance des erreurs :** Sentry
*   **Conteneurisation :** Docker
*   **CI/CD :** GitLab CI 
*   **Gestion des variables d'environnement :** python-dotenv

La liste complète des dépendances Python se trouve dans le fichier `requirements.txt`.

## 4. Prérequis

Avant de commencer, assurez-vous d'avoir installé :

*   Python (version compatible, ex: 3.9+)
*   pip (généralement inclus avec Python)
*   Git
*   Docker et Docker Compose (pour la conteneurisation et le lancement via Docker)
*   Un compte Docker Hub (pour la publication d'images)
*   Un compte sur l'hébergeur Render
*   Un compte Sentry et un DSN (Data Source Name) pour la surveillance des erreurs.

## 5. Installation

Suivez ces étapes pour configurer l'environnement de développement local.

### Clonage du Dépôt

```bash
git clone https://gitlab.com/ansilema-group/Python-OC-Lettings-FR.git
cd oc-lettings-site # ou le nom du dossier du projet
```
### Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate
```

### Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Configurer les variables d’environnement

L'application utilise des variables d'environnement pour la configuration. Créez un fichier `.env` à la racine du projet en vous basant sur le fichier

**Exemple de contenu du fichier `.env` :**

```env
SECRET_KEY='VOTRE_CLE_SECRETE_DJANGO_ICI'

ALLOWED_HOSTS=localhost,127.0.0.1 # Optionnel pour le dev local, crucial en prod

SENTRY_DSN='votre_dsn_sentry_ici'
```

#### Générer la `SECRET_KEY` Django

La `SECRET_KEY` est une chaîne de caractères longue et aléatoire utilisée par Django pour diverses opérations de sécurité. Elle doit être unique à votre installation et gardée secrète.

**Pour générer une nouvelle `SECRET_KEY` :**

1. Ouvrez votre terminal ou invite de commandes et exécutez la commande Python suivante :

    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

2. Cette commande affichera une chaîne de caractères aléatoire, par exemple :
    `'abC123xyz!@#pqrStuv789defGHIjklMNO456'`

4.  Copiez **l'intégralité de cette chaîne générée** (y compris les apostrophes, si présentes) et collez-la comme valeur pour `SECRET_KEY` dans votre fichier `.env` :

    ```env
    # Fichier .env
    # ... autres variables ...
    SECRET_KEY='abC123xyz!@#pqrStuv789defGHIjklMNO456' # Remplacez par VOTRE clé générée
    # ...
    ```

**IMPORTANT :**
*   Ne committez **jamais** votre fichier `.env` contenant la `SECRET_KEY` (ou toute autre information sensible) dans un dépôt Git public. Le fichier `.gitignore` devrait déjà inclure `.env`.

---

## 6. Démarrage Rapide (Lancement Local)

Après avoir suivi les étapes d'[Installation](#installation) et configuré votre fichier `.env` :

1.  Appliquez les migrations de la base de données :
    ```bash
    python manage.py migrate
    ```
2.  Lancez le serveur de développement Django :
    ```bash
    python manage.py runserver
    ```
L'application sera alors accessible à l'adresse `http://127.0.0.1:8000/`.

## 7. Tests et Qualité du Code

Pour assurer la qualité et la robustesse du code :

*   **Vérifier la qualité du code (Linting avec Flake8) :**
    La configuration de Flake8 se trouve dans `.flake8` (ou `setup.cfg`).
    ```bash
    flake8 .
    ```
*   **Lancer les tests unitaires et la couverture (Pytest & Coverage) :**
    ```bash
    coverage run -m pytest
    coverage report --fail-under=80
    ```
    La couverture de test doit être supérieure à 80%. Un rapport HTML détaillé est généré dans le dossier `htmlcov/`.

## 8. Surveillance et Gestion des Erreurs (Sentry)

Pour assurer un suivi proactif des erreurs en production et faciliter le débogage, l'application intègre Sentry, un service de surveillance des erreurs en temps réel. Le module `logging` standard de Python est également utilisé de manière stratégique pour enrichir les informations envoyées à Sentry et pour le logging local.

### 8.1 Configuration de Sentry

1.  **DSN Sentry :** La connexion à Sentry est établie via un DSN (Data Source Name). Cette clé doit être définie comme une variable d'environnement nommée `SENTRY_DSN`.
    *   En local, ajoutez `SENTRY_DSN='VOTRE_DSN_SENTRY_POUR_DEV_OU_TEST'` à votre fichier `.env`.
    *   En production (sur Render, par exemple), configurez `SENTRY_DSN` dans les variables d'environnement du service.
2.  **Initialisation dans Django :** Sentry est initialisé dans `oc_lettings_site/settings.py`. La configuration inclut typiquement :
    *   `sentry_sdk.init(...)`
    *   `DjangoIntegration()`: Pour capturer automatiquement les exceptions non gérées dans Django.
    *   `LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)`: Pour envoyer les messages de log Python à Sentry. Les logs de niveau `INFO` et supérieurs sont traités, mais seuls ceux de niveau `ERROR` (ou plus critique) sont envoyés comme des événements distincts à Sentry.

### 8.2 Stratégie de Logging dans l'Application

Le module `logging` de Python est utilisé pour enregistrer des informations pertinentes à différents niveaux :

*   **`logger = logging.getLogger(__name__)`**: Chaque module significatif (vues, middleware) utilise son propre logger pour une meilleure granularité.

*   **Niveau `INFO` :** Utilisé pour tracer le déroulement normal des opérations. Ces logs sont utiles pour comprendre le flux d'une requête mais ne sont généralement pas envoyés comme des événements distincts à Sentry (sauf s'ils sont inclus comme "breadcrumbs" dans un événement d'erreur).
    *   Exemple dans `lettings/views.py` et `profiles/views.py` :
        ```python
        logger.info("Lettings index page requested")
        logger.info(f"Profile requested for user {username}")
        ```

*   **Niveau `ERROR` :** Utilisé pour signaler des problèmes qui empêchent une opération de se terminer correctement ou indiquent une situation anormale. Ces logs sont généralement configurés pour être envoyés à Sentry comme des événements.
    *   Exemple dans `profiles/views.py` lors d'une erreur de récupération de profil :
        ```python
        try:
            profile = get_object_or_404(Profile, user__username=username)
            # ...
        except Exception as e:
            logger.error(f"Error retrieving profile for user {username}: {e}")
            raise
        ```

### 8.3 Middleware de Surveillance (`monitoring/monitoring_middleware.py`)

Un middleware personnalisé, `ExceptionLoggingMiddleware`, a été mis en place pour améliorer la journalisation des erreurs HTTP :

*   Il intercepte toutes les requêtes et réponses.
*   Si une réponse a un **code de statut >= 400** (par exemple, 401 Unauthorized, 403 Forbidden, 500 Internal Server Error), le middleware enregistre une erreur avec `logger.error()`:
    ```python
    if response.status_code >= 400:
        logger.error(f"HTTP {response.status_code} error at {request.path}")
    ```
*   Il capture spécifiquement les exceptions `Http404` (par exemple, levées par `get_object_or_404`), les enregistre avec `logger.error()`, puis les relève pour que Django puisse afficher la page 404 :
    ```python
    except Http404 as e:
        logger.error(f"404 error at {request.path}: {str(e)}")
        raise
    ```

### 8.4 Ce que Sentry Capture

Grâce à cette configuration :

1.  **Exceptions Python non gérées :** Capturées automatiquement par `DjangoIntegration`.
2.  **Erreurs HTTP (400+) :** Les erreurs HTTP détectées par le `ExceptionLoggingMiddleware` sont loguées comme `ERROR` et donc envoyées à Sentry. Cela inclut les erreurs 404.
3.  **Erreurs Spécifiques Loguées :** Toute utilisation de `logger.error()` ou `logger.critical()` dans le code (comme dans le `try/except` de `profiles/views.py`) sera également envoyée à Sentry.

---

## 9. Utilisation avec Docker

L'application peut être construite et exécutée via Docker.

*   **Construire et lancer l'image Docker localement :**
    1.  Construire l'image :
        ```bash
        docker build -t python-oc-lettings-fr .
        ```
    2.  Lancer un conteneur depuis l'image (assurez-vous que votre fichier `.env` est présent à la racine du projet pour être utilisé par `--env-file`) :
        ```bash
        docker run --rm -p 8000:8000 --env-file .env python-oc-lettings-fr
        ```
*   **Lancer l'image depuis Docker Hub (via Makefile) :**
    Si une image `:latest` est disponible sur Docker Hub et que le `Makefile` est configuré pour cela :
    ```bash
    make run-latest
    ```
    Cela suppose que le `Makefile` contient une cible qui effectue un `docker pull` puis `docker run` de l'image appropriée.

## 10. Déploiement et Pipeline CI/CD

Le déploiement de l'application est automatisé via un pipeline CI/CD.

### 10.1 Aperçu du Pipeline (GitLab CI/CD & Render)

Le projet utilise un pipeline CI/CD configuré via `.gitlab-ci.yml` (pour GitLab) qui interagit avec Docker Hub et Render :

1.  ✅ **Tests et Linting :** Sur chaque `push` vers n'importe quelle branche, `flake8` et `pytest` (avec vérification de la couverture > 80%) sont exécutés.
2.  🐳 **Conteneurisation :** Si les tests et le linting réussissent sur la branche `master`, une image Docker est construite et poussée sur Docker Hub (ex: `votrenomdocker/python-oc-lettings-fr:latest`).
3.  🌍 **Déploiement sur Render :** Render est configuré pour surveiller cette image sur Docker Hub. Dès qu'une nouvelle version `:latest` est disponible, Render récupère l'image et déploie automatiquement le site.

Ce processus garantit que seul du code testé et validé est mis en production.

### 10.2 Configuration Requise pour le Déploiement

Pour que le pipeline et le déploiement fonctionnent correctement :

*   **Variables d'environnement (Local - `.env`) :** Pour le développement et les tests locaux.
*   **Variables d'environnement (GitLab CI - _Settings > CI/CD > Variables_) :**
    *   `DOCKER_USERNAME`: Votre nom d'utilisateur Docker Hub.
    *   `DOCKER_PASSWORD` (ou `DOCKER_TOKEN`): Votre mot de passe ou token d'accès Docker Hub avec droits d'écriture.
*   **Variables d'environnement (Render - _Environment_) :**
    *   `SECRET_KEY`: Clé Django secrète **forte et unique** pour la production.
    *   `DEBUG=False`
    *   `ALLOWED_HOSTS`: Doit inclure votre domaine Render (ex: `python-oc-lettings-fr.onrender.com`) et tout domaine personnalisé.
    *   `SENTRY_DSN`: (Optionnel) Votre DSN Sentry pour le monitoring des erreurs en production.
    *   `DATABASE_URL`: (Si vous utilisez une base de données managée par Render ou externe) L'URL de connexion.
    *   Autres variables nécessaires (ex: `PYTHON_VERSION`, `PORT`).
*   **Docker Hub :**
    *   Un dépôt (repository) public ou privé pour héberger vos images Docker (ex: `votrenomdocker/python-oc-lettings-fr`).
*   **Render :**
    *   Un "Web Service" configuré pour utiliser une "Existing Docker Image" pointant vers votre image sur Docker Hub.
    *   L'option "Auto-Deploy" activée pour se redéployer automatiquement lors de la mise à jour de l'image taguée `:latest`.
    *   Commande de démarrage configurée (ex: `gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT`, potentiellement précédée de `python manage.py migrate` et `python manage.py collectstatic --noinput`).

### 10.3 Processus de Déploiement (via la branche `master`)

Le déploiement en production est typiquement déclenché par un push sur la branche `master`.

1.  **Fusionnez vos modifications dans `master` et poussez :**
    ```bash
    git checkout master
    git merge votre-branche-de-fonctionnalite
    # Résoudre les conflits si nécessaire
    git pull origin master # S'assurer d'être à jour avec la branche distante
    git push origin master
    ```
2.  **Suivez le pipeline dans GitLab (`CI/CD > Pipelines`) :**
    *   Vérifiez que les étapes de linting (`flake8`) et de tests (`test`) passent. ✅
    *   Vérifiez que l'étape de construction et de push de l'image Docker (`docker-build` ou nom similaire) se termine avec succès. ✅
3.  **Vérifiez le déploiement sur Render :**
    *   Connectez-vous à votre tableau de bord Render.
    *   Le service concerné devrait indiquer un nouveau déploiement en cours ou récemment terminé, initié par la mise à jour de l'image Docker sur Docker Hub.
4.  **Vérifications post-déploiement dans le navigateur :**
    *   Accédez à l'URL de production de votre site.
    *   Vérifiez le bon chargement de la page d'accueil et d'autres pages clés.
    *   Assurez-vous que les fichiers statiques (CSS, JS, images) se chargent correctement et que le style est conforme.
    *   Testez l'accès et l'apparence de l'interface d'administration (`/admin/`).
    *   Si Sentry est configuré, vérifiez (par exemple en provoquant une erreur test) que les erreurs remontent bien.
