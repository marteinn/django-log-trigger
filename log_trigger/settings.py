from django.conf import settings


LOGGER_NAME = getattr(settings, 'LOG_TRIGGERS_LOGGER_NAME',
                      'log_triggers.views')
LOGGER_SECRET = getattr(settings, 'LOG_TRIGGERS_SECRET', '')
