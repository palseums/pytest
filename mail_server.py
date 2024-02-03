import requests
import unittest
from unittest.mock import patch,Mock
from module1 import patch1,method1,Class1

def get_data():
    pass

def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")

    return response.join()

class TestUserData(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_data(self,mock_get):
        mock_response = Mock()
        response_dict = {'name': 'Palani','email': 'palani@gmail.com'}
        mock_response.join.return_value = response_dict
        mock_get.return_value = mock_response
        assert get_user_data(1) == response_dict


