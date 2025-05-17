Interfaces de programmation
=================================

Le projet **Python-OC-Lettings-FR** repose sur des vues Django classiques (views basées sur des fonctions) et une structure en URLs bien définie.

Organisation
------------

Le projet se compose des modules suivants :

- ``oc_lettings_site`` : contient les routes globales et les vues pour la page d’accueil et les erreurs personnalisées (404, 500).
- ``profiles`` : contient les vues et URL pour la gestion des profils utilisateurs.
- ``lettings`` : contient les vues et URL pour la gestion des locations.

Routes principales
------------------

Page d’accueil :
^^^^^^^^^^^^^^^^
- **URL** : `/`
- **Vue** : `index`
- **Description** : Affiche la page d’accueil de l’application.

Profils :
^^^^^^^^^
- **URL** : `/profiles/`
- **Vue** : `profiles_index`
- **Description** : Liste tous les profils d’utilisateurs.

- **URL** : `/profiles/<username>/`
- **Vue** : `profile`
- **Description** : Affiche le détail d’un profil utilisateur.

Locations :
^^^^^^^^^^^
- **URL** : `/lettings/`
- **Vue** : `lettings_index`
- **Description** : Liste toutes les locations disponibles.

- **URL** : `/lettings/<id>/`
- **Vue** : `letting`
- **Description** : Affiche le détail d’une location donnée.

Gestion des erreurs
-------------------
- **404** : Page non trouvée → Vue `custom_404`
- **500** : Erreur serveur → Vue `custom_500`

Toutes ces vues sont accessibles via des liens dans la page d'accueil ou directement via les URLs indiquées ci-dessus.

Middleware personnalisé
-----------------------

Le projet intègre un middleware `ExceptionLoggingMiddleware` dans le module `monitoring`, qui intercepte les erreurs HTTP 400+ et les envoie à Sentry tout en les enregistrant via le module `logging`.