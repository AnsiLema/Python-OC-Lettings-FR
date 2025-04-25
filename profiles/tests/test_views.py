import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_detail_view(client):
    user = User.objects.create_user(username='testuser', password='password123')
    Profile.objects.create(user=user, favorite_city='Paris')

    url = reverse('profiles:profile', args=['testuser'])
    response = client.get(url)

    assert response.status_code == 200
    assert b'Paris' in response.content


@pytest.mark.django_db
def test_profile_detail_view_404(client):
    url = reverse('profiles:profile', args=['nonexistentuser'])
    response = client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_profiles_index_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    Profile.objects.create(user=user, favorite_city='Paris')

    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == 200
    assert b'testuser' in response.content