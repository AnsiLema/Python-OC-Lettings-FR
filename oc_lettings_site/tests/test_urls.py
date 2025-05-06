from django.urls import reverse, resolve
from oc_lettings_site.views import index as oc_lettings_index_view


def test_index_url_resolves():
    url = reverse('index')
    resolver = resolve(url)
    assert resolver.func == oc_lettings_index_view
    assert resolver.view_name == 'index'
