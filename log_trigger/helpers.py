import logging

from log_trigger import settings


def get_logger():
    return logging.getLogger(settings.LOGGER_NAME)


def validate_secret(request):
    if not settings.LOGGER_SECRET:
        return True

    secret = request.GET.get('secret', '')
    if secret != settings.LOGGER_SECRET:
        return False

    return True
