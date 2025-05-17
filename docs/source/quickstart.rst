Guide de démarrage rapide
=========================

Pour exécuter rapidement le projet via Docker :

.. code-block:: bash

   make run-latest

Cela va :

- Récupérer la dernière image Docker du projet,
- Lancer l'application sur `http://localhost:8001`,
- Charger automatiquement les variables d’environnement depuis `.env`.

Assurez-vous d’avoir `Docker` et `make` installés.