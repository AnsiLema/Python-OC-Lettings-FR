Modèles de données
==================

Cette section détaille les principaux modèles utilisés dans le projet Python OC Lettings FR. Ces modèles définissent la structure de la base de données via Django ORM.

Profile
-------

Le modèle ``Profile`` est utilisé pour stocker des informations supplémentaires liées à un utilisateur.

.. code-block:: python

   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       favorite_city = models.CharField(max_length=64, blank=True)

Chaque profil est lié à un utilisateur Django natif. Il peut contenir des informations personnalisées comme la ville préférée.

Letting
-------

Représente une location disponible. Il est lié à une adresse.

.. code-block:: python

   class Letting(models.Model):
       title = models.CharField(max_length=256)
       address = models.OneToOneField(Address, on_delete=models.CASCADE)

Address
-------

Le modèle ``Address`` est utilisé pour stocker les informations d’adresse de chaque location.

.. code-block:: python

   class Address(models.Model):
       number = models.PositiveIntegerField()
       street = models.CharField(max_length=64)
       city = models.CharField(max_length=64)
       state = models.CharField(max_length=2)
       zip_code = models.PositiveIntegerField()
       country_iso_code = models.CharField(max_length=3)

Organisation des données
------------------------

- Chaque ``Letting`` possède une ``Address`` unique.
- Chaque ``Profile`` est associé à un ``User`` Django.
- Les relations entre les modèles sont gérées automatiquement par l’ORM de Django.
- Les données sont stockées dans une base SQLite par défaut (configurable).