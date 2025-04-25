from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Represents a physical address.

    This class is used to store information about physical addresses, such as the
    street, city, state, postal code, and country. It includes constraints to
    validate the attributes like the length of state and country ISO codes or the
    maximum values for number and postal code. The address can be represented as
    a formatted string through its string conversion method.

    :ivar number: The building number in the address.
    :type number: PositiveIntegerField
    :ivar street: The name of the street in the address.
    :type street: CharField
    :ivar city: The city of the address.
    :type city: CharField
    :ivar state: The two-character state code for the address.
    :type state: CharField
    :ivar zip_code: The postal code of the address.
    :type zip_code: PositiveIntegerField
    :ivar country_iso_code: The three-character ISO code for the country.
    :type country_iso_code: CharField

    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a Letting entity.

    The Letting entity stores information about a specific letting, including its
    title and associated address. It uses Django's ORM framework for database
    interaction.

    :ivar title: The title of the letting.
    :type title: str
    :ivar address: The associated address for the letting.
    :type address: Address
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "lettings"

    def __str__(self):
        return self.title
