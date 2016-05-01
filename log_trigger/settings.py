from django.conf import settings


LOGGER_NAME = getattr(settings, 'LOG_TRIGGER_LOGGER_NAME',
                      'log_trigger.views')
LOGGER_SECRET = getattr(settings, 'LOG_TRIGGER_SECRET', '')
