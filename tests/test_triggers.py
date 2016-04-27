from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class LogTriggerViewTests(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_system_exception_trigger(self):
        """
        Makes sure view raises fatal error
        """
        with self.assertRaises(SystemExit) as ex:
            self.client.get(reverse('log_trigger:system_exception_view'))
            self.assertEqual(ex.exception, 'System Exit')
