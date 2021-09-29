from lahar import Client
from unittest import TestCase


class LaharClientGetUrlTest(TestCase):
    def setUp(self):
        self.lahar = Client('lahar-api-token')

    def test_concat_base_url_endpoint(self):
        expected = 'http://app.lahar.com.br/api/conversions'
        self.assertEqual(expected, self.lahar.get_url('/conversions'))

    def test_concat_base_url_trailing_slash_endpoint(self):
        expected = 'http://app.lahar.com.br/api/conversions'
        self.assertEqual(expected, self.lahar.get_url('conversions'))


class LaharClientGetHashesTest(TestCase):
    def setUp(self):
        self.lahar = Client('lahar-api-token')

    def test_get_token_hash(self):
        expected = {'token_api_lahar': 'lahar-api-token'}
        self.assertEqual(expected, self.lahar.get_token_hash())

    def test_get_default_event_hash(self):
        expected = {'nome_formulario': 'integration'}
        self.assertEqual(expected, self.lahar.get_event_hash())

    def test_prepare_data(self):
        data = dict(email='valid@email.com')
        expected = {
            'token_api_lahar': 'lahar-api-token',
            'email': 'valid@email.com'
        }
        self.assertEqual(expected, self.lahar._prepare_data(data))
