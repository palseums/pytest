from unittest import mock,TestCase

import facebook
import google


class TestApi(TestCase):

    @mock.patch('facebook.get_data',return_value='data_3')
    @mock.patch('google.get_data',return_value='data_2')
    def test_external_api(self,googl,fb):
        self.assertEqual(google.call_google_api(),'data_2')
        self.assertEqual(facebook.call_facebook_api(),'data_3')

    def test_external_api1(self):
        with mock.patch('google.get_data',return_value='data_2'):
            self.assertEqual(google.call_google_api(),'data_2')
