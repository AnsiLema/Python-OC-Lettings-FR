import pytest
from django.http import Http404, HttpResponse
from django.test import RequestFactory
from monitoring.monitoring_middleware import ExceptionLoggingMiddleware


@pytest.fixture
def get_response_mock():
    def _mock_response(request):
        return HttpResponse(status=200)

    return _mock_response


@pytest.fixture
def middleware_instance(get_response_mock):
    return ExceptionLoggingMiddleware(get_response_mock)


def test_middleware_process_request_success(middleware_instance):
    """
    Tests that the middleware processes a request successfully without logging any error
    when there is no exception and the response status code is below 400.
    """
    rf = RequestFactory()
    request = rf.get("/test-url/")

    response = middleware_instance(request)

    assert response.status_code == 200


def test_middleware_logs_error_for_400_status_code(middleware_instance, caplog):
    """
    Tests that the middleware logs an error for a response
    with a 400 status code.
    """

    def mock_get_response_400(request):
        return HttpResponse(status=400)

    middleware_instance.get_response = mock_get_response_400

    rf = RequestFactory()
    request = rf.get("/test-error/")

    with caplog.at_level("ERROR"):
        middleware_instance(request)

    # Vérifie qu’un message d’erreur a bien été loggé
    assert any("HTTP 400 error at /test-error/" in message for message in caplog.messages)


def test_middleware_logs_and_reraises_404_exception(middleware_instance):
    """
    Tests that the middleware logs a 404 error and re-raises the Http404 exception.
    """

    def mock_get_response_404(request):
        raise Http404("Not found")

    middleware_instance.get_response = mock_get_response_404

    rf = RequestFactory()
    request = rf.get("/test-404/")

    with pytest.raises(Http404):
        middleware_instance(request)
