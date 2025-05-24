import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_lettings_index_status_code(client):
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_view(client):
    # Créer une adresse fictive
    address = Address.objects.create(
        number=123,
        street='Rue Test',
       # city='Villetest',
        state='DP',
        zip_code=75000,
        country_iso_code='FR'
    )

    # Créer un letting lié à cette adresse
    letting = Letting.objects.create(
        title='Appartement Test',
        address=address
    )

    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)

    assert response.status_code == 200
    assert b'Appartement Test' in response.content
    assert b'Rue Test' in response.content


@pytest.mark.django_db
def test_letting_detail_view_404(client):
    url = reverse('lettings:letting', args=[999])  # ID inexistant
    response = client.get(url)
    assert response.status_code == 404
