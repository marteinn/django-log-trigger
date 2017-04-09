from django.core.urlresolvers import reverse
from django.test.utils import patch_logger
from django.test import SimpleTestCase, override_settings
from django.utils.log import (
    DEFAULT_LOGGING
)


@override_settings(DEBUG=True)
class ExceptionTests(SimpleTestCase):
    def test_system_exception_trigger(self):
        """
        Makes sure view raises fatal error
        """
        with self.assertRaises(SystemExit) as ex:
            self.client.get(reverse('log_trigger:system_exception_view'))
            self.assertEqual(ex.exception, 'System Exit')

    # def test_unhandled_exception_trigger(self):
        # """
        # Makes sure view raises fatal error
        # """
        # with self.assertRaises(Exception) as ex:
            # self.client.get(reverse('log_trigger:unhandled_exception_view'))
            # self.assertEqual(ex.exception, 'Unhandled Exception')

    def test_disallowed_host_exception_trigger(self):
        """
        Makes sure disallowed host gets captured
        """
        with patch_logger('django.security.DisallowedHost', 'error') as calls:
            self.client.get(reverse('log_trigger:disallowed_host_exception_view'))  # NOQA
            self.assertEqual(len(calls), 1)
            self.assertEqual(calls[0], 'DisallowedHost Exception')


LOGGING = DEFAULT_LOGGING['loggers'] = {
    'log_trigger.views': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


@override_settings(DEBUG=True, LOGGING=LOGGING)
class LoggerTests(SimpleTestCase):
    def test_logger_debug_view(self):
        """
        Makes sure debug messages are captured
        """
        with patch_logger('log_trigger.views', 'debug') as calls:
            self.client.get(reverse('log_trigger:logger_debug_view'))  # NOQA
            self.assertEqual(calls[0], 'Debug message')

    def test_logger_info_view(self):
        """
        Makes sure info messages are captured
        """
        with patch_logger('log_trigger.views', 'info') as calls:
            self.client.get(reverse('log_trigger:logger_info_view'))  # NOQA
            self.assertEqual(calls[0], 'Info message')

    def test_logger_warn_view(self):
        """
        Makes sure debug messages are captured
        """
        with patch_logger('log_trigger.views', 'warn') as calls:
            self.client.get(reverse('log_trigger:logger_warn_view'))  # NOQA
            self.assertEqual(calls[0], 'Warn message')

    def test_logger_error_view(self):
        """
        Makes sure error messages are captured
        """
        with patch_logger('log_trigger.views', 'error') as calls:
            self.client.get(reverse('log_trigger:logger_error_view'))  # NOQA
            self.assertEqual(calls[0], 'Error message')

    def test_logger_critical_view(self):
        """
        Makes sure critical messages are captured
        """
        with patch_logger('log_trigger.views', 'critical') as calls:
            self.client.get(reverse('log_trigger:logger_critical_view'))  # NOQA
            self.assertEqual(calls[0], 'Critical message')
