from django.shortcuts import render


def index(request):
    """
    Handles the HTTP request to render the index page.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The rendered HTML for the index page.
    :rtype: HttpResponse
    """
    return render(request, 'index.html')

def custom_404(request, exception):
    """
    Custom handler for the HTTP 404 error.

    This function is responsible for rendering a specific template
    (404.html) to provide a user-friendly error message whenever a
    requested resource is not found (HTTP 404).

    :param request: The HttpRequest object representing the current
        web request.
    :type request: HttpRequest
    :param exception: The exception that triggered the 404 error.
    :type exception: Exception
    :return: A rendered response object with a 404 HTTP status code.
    :rtype: HttpResponse
    """
    return render(request, '404.html',status=404)

def custom_500(request):
    """
    Handles the rendering of the custom 500 error page.

    This function processes a request and returns an HTTP response rendering
    a custom 500 error template. The status code of the response is set
    to 500 to indicate an internal server error.

    :param request: The HttpRequest object for the current request.
    :return: An HttpResponse object with the rendered 500 error template
        and a status code of 500.
    """
    return render(request, '500.html', status=500)