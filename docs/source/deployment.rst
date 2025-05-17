Déploiement et gestion de l’application
=======================================

Cette section décrit les étapes pour déployer et maintenir l’application Python OC Lettings FR en environnement de production.

Environnement cible
-------------------

L’application est déployée sur :

- **Render.com** (hébergeur)
- Docker Hub (registre d’images Docker)
- GitLab CI/CD (gestion du pipeline de déploiement)

Pipeline CI/CD
--------------

Le pipeline GitLab comprend 3 étapes :

1. **Tests** (linting avec Flake8, tests avec Pytest et couverture > 80 %)
2. **Build Docker** (création et push de l’image vers Docker Hub)
3. **Déploiement** (déclenché automatiquement depuis la branche `master`)

Seule la branche `master` déclenche la conteneurisation + déploiement. Les autres branches n'exécutent que les tests.

Configuration requise
----------------------

Les variables d’environnement suivantes doivent être définies :

- `DEBUG`
- `SECRET_KEY`
- `SENTRY_DSN`
- `ALLOWED_HOSTS`

Dans Render, ces variables sont à déclarer dans **Settings > Environment > Environment Variables**.

Fichiers de configuration utilisés :

- `.gitlab-ci.yml` : pipeline CI/CD
- `Dockerfile` : construction de l’image
- `.env` : configuration locale


Commandes utiles (en local)
----------------------------

- **Lancer l’image Docker :**

.. code-block:: bash

   make run-latest

- **Construire l’image manuellement :**

.. code-block:: bash

   docker build -t <tag> .

- **Lancer l’app localement avec un .env :**

.. code-block:: bash

   docker run --rm --env-file .env -p 8000:8000 <image>

Gestion des fichiers statiques
------------------------------

L’application utilise **Whitenoise** pour servir les fichiers statiques.

En production :

.. code-block:: bash

   python manage.py collectstatic --noinput

Les fichiers sont copiés vers `staticfiles/` et servis directement par Gunicorn via Whitenoise.

Surveillance et journalisation
------------------------------

- **Sentry** est intégré à Django pour capturer les erreurs.
- Les erreurs critiques (404, 500, exceptions non gérées) sont automatiquement envoyées à Sentry.
- Un middleware personnalisé journalise également toutes les erreurs 4xx/5xx.

Mise à jour
-----------

Toute modification poussée sur `master` :

- Relance les tests
- Reconstruit une image Docker
- Push sur Docker Hub
- Déclenche un redéploiement sur Render