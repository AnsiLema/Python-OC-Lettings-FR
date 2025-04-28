import logging

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Profile


logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the profiles index page with a list of all profiles.

    The function retrieves all existing Profile objects and passes them as context
    to the 'profiles/index.html' template.

    :param request: Django HTTP request object.
    :type request: HttpRequest
    :return: Rendered HTML response for the profiles index page.
    :rtype: HttpResponse
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Retrieves user profile based on the provided username and renders the
    profile view.

    This function fetches the Profile object associated with the specified
    username, prepares the context for rendering, and uses the Django render
    method to return a response to the corresponding template.

    :param request: HttpRequest object representing the current request.
    :type request: HttpRequest
    :param username: Username associated with the desired user profile.
    :type username: str
    :return: HttpResponse object rendering the profile view.
    :rtype: HttpResponse
    """
    logger.info(f"Profile requested for user {username}")

    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info(f"Profile successfully retrieved for user {username}")
    except Exception as e:
        logger.error(f"Error retrieving profile for user {username}: {e}")
        raise

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
