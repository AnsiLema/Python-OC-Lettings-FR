import logging
from django.http import Http404

logger = logging.getLogger(__name__)

class ExceptionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            if response.status_code >= 400:
                logger.error(f"HTTP {response.status_code} error at {request.path}")
            return response
        except Http404 as e:
            logger.error(f"404 error at {request.path}: {str(e)}")
            raise