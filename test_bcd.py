import fetch_www
from fetch_www import parse
from unittest.mock import patch


@patch('fetch_www.fetch_net')
def test_parse(mock_get):
    mock_get.return_value = 'def'
    assert parse() == "def123"