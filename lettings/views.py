from django.shortcuts import render
from .models import Letting
from django.shortcuts import get_object_or_404

def index(request):
    """
    Handles the retrieval and rendering of the list of lettings.

    This function fetches all lettings from the database using the Letting
    model and renders them in the specified template along with the
    necessary context.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: An HttpResponse object that renders the "lettings/index.html"
        template with the context containing the list of lettings.
    :rtype: HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Fetch and display a specific letting detail page based on the letting ID provided.

    This function retrieves a letting object using the given ID and renders a template
    with the letting's information, including its title and address. The resulting
    HTML page will provide users with details about the selected letting.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param letting_id: The unique identifier of the letting to retrieve.
    :type letting_id: int
    :return: Rendered HTML response displaying the letting details.
    :rtype: HttpResponse
    """
    letting = get_object_or_404(Letting, pk=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
