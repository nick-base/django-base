from django.test import TestCase
from django.utils import translation


class I18nTestCase(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        self.assertEqual(translation.gettext('app root'), 'app root zh')
