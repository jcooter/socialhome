from unittest.mock import Mock

from rest_framework.test import APITestCase
from test_plus import TestCase
from test_plus.test import CBVTestCase

import socialhome.tests.environment  # Set some environment tweaks


class SocialhomeTestCase(TestCase):
    maxDiff = None


class SocialhomeCBVTestCase(CBVTestCase):
    maxDiff = None


class SocialhomeAPITestCase(APITestCase):
    maxDiff = None


# py.test monkeypatches while we still have two kinds of tests
# Remove these once all our tests are either `SocialhomeTestCase` or another test class
def disable_requests(monkeypatch):
    """Mock away request.get and requests.post."""
    monkeypatch.setattr("requests.post", Mock())

    class MockResponse(str):
        status_code = 200
        text = ""

        @staticmethod
        def raise_for_status():
            pass

    monkeypatch.setattr("requests.get", Mock(return_value=MockResponse))


def disable_mailer(monkeypatch):
    """Mock away mail sending."""
    monkeypatch.setattr("django.core.mail.send_mail", Mock())
