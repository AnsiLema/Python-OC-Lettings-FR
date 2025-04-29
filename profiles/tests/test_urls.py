from django.urls import reverse, resolve
from profiles.views import index as profiles_index_view
from profiles.views import profile as profiles_profile_view


def test_profiles_index_url_resolves():
    url = reverse('profiles:index')
    resolver = resolve(url)
    assert resolver.func == profiles_index_view
    assert resolver.view_name == 'profiles:index'

def test_profile_detail_url_resolves():
    url = reverse('profiles:profile', args=['testuser'])
    resolver = resolve(url)
    assert resolver.func == profiles_profile_view
    assert resolver.view_name == 'profiles:profile'