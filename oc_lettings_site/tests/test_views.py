import pytest
from django.urls import reverse
from django.test import RequestFactory
from oc_lettings_site.views import custom_404
from oc_lettings_site.views import custom_500


@pytest.mark.django_db
def test_homepage_status_code(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_custom_404_view_renders_template():
    factory = RequestFactory()
    request = factory.get('/wrong-url/')

    # response = custom_404(request, exception=Exception('Not Found!'))
    assert response.status_code == 404
    assert b"Page" in response.content or b"404" in response.content


@pytest.mark.django_db
def test_custom_500_view_renders_template():
    factory = RequestFactory()
    request = factory.get('/trigger-500-error/')
    response = custom_500(request)
    assert response.status_code == 500
    assert b"Page" in response.content or b"500" in response.content
