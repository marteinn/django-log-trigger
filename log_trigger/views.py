from django.http import HttpResponse
from django.core.exceptions import DisallowedHost

from log_trigger.helpers import get_logger, validate_secret


unauthorized_response = HttpResponse('Unauthorized', status=401)


def system_exception_view(request):
    if not validate_secret(request):
        return unauthorized_response

    raise SystemExit('System Exit')


def unhandled_exception_view(request):
    if not validate_secret(request):
        return unauthorized_response

    raise Exception('Unhandled Exception')


def disallowed_host_exception_view(request):
    if not validate_secret(request):
        return unauthorized_response

    raise DisallowedHost('DisallowedHost Exception')


def logger_debug_view(request):
    if not validate_secret(request):
        return unauthorized_response

    get_logger().debug('Debug message')
    return HttpResponse('Debug message')


def logger_info_view(request):
    if not validate_secret(request):
        return unauthorized_response

    get_logger().info('Info message')
    return HttpResponse('Info message')


def logger_warn_view(request):
    if not validate_secret(request):
        return unauthorized_response

    get_logger().warn('Warn message')
    return HttpResponse('Warn message')


def logger_error_view(request):
    if not validate_secret(request):
        return unauthorized_response

    get_logger().error('Error message')
    return HttpResponse('Error message')


def logger_critical_view(request):
    if not validate_secret(request):
        return unauthorized_response

    get_logger().critical('Critical message')
    return HttpResponse('Critical message')
