from django.urls import reverse, resolve
from lettings.views import index as lettings_index_view
from lettings.views import letting as lettings_detail_view

def test_lettings_index_url_resolves():
    """
    Tests that the 'lettings:index' URL resolves to the correct view and view name.

    This function validates the resolution of the provided URL for the 'lettings:index'
    route to ensure that it resolves as expected to the `lettings_index_view`. It also
    checks that the view name returned by the resolver matches the specified view name.

    :return: None
    """
    url = reverse('lettings:index')
    resolver = resolve(url)
    assert resolve(url).func == lettings_index_view
    assert resolver.view_name == 'lettings:index'

def test_letting_detail_url_resolves():
    """
    Tests that the URL for the letting detail view resolves correctly and matches the
    expected view function and view name.

    This test ensures that the reverse-resolved URL for the letting detail correctly
    maps to the corresponding view function and that the resolved view name matches
    the expected name.

    :return: None
    """
    url = reverse('lettings:letting', kwargs={'letting_id': 1})
    resolver = resolve(url)
    assert resolve(url).func == lettings_detail_view
    assert resolver.view_name == 'lettings:letting'