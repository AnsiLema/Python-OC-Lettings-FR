import logging
from django.http import Http404

logger = logging.getLogger(__name__)


class ExceptionLoggingMiddleware:
    """
    Middleware for logging exceptions and HTTP errors.

    This middleware intercepts HTTP requests and responses to log significant
    errors, such as HTTP 404 errors or any response with a status code of 400
    or higher. It is designed to provide better insight into issues occurring
    during request processing. The middleware does not alter the response or
    request content except for logging purposes.

    :ivar get_response: The next middleware or view callable in the middleware
        chain.
    :type get_response: Callable
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Handles incoming HTTP requests, logs errors for responses with status codes
        400 or higher, and re-raises 404 errors after logging them.

        :param request: The HTTP request object to process.
        :type request: django.http.HttpRequest
        :return: The HTTP response object generated after processing the request.
        :rtype: django.http.HttpResponse
        :raises Http404: If the requested resource is not found.
        """
        try:
            response = self.get_response(request)
            if response.status_code >= 400:
                logger.error(f"HTTP {response.status_code} error at {request.path}")
            return response
        except Http404 as e:
            logger.error(f"404 error at {request.path}: {str(e)}")
            raise
