Installation
============

1. Cloner le projet :

   .. code-block:: bash

       git clone https://gitlab.com/ansilema-group/Python-OC-Lettings-FR.git
       cd Python-OC-Lettings-FR

2. Créer et activer un environnement virtuel :

   .. code-block:: bash

       python -m venv .venv
       source .venv/bin/activate

3. Installer les dépendances :

   .. code-block:: bash

       pip install -r requirements.txt

4. Lancer les migrations (optionnel en local) :

   .. code-block:: bash

       python manage.py migrate

5. Lancer le serveur de développement :

   .. code-block:: bash

       python manage.py runserver