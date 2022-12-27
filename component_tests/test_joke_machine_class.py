import pytest
from joke_machine import ConnectionToJokeAPI
from unittest.mock import MagicMock, patch
from unittest import mock

def test_connection():
        obj = ConnectionToJokeAPI()
        assert obj.joke_api.status_code == 200

@mock.patch('joke_machine.ConnectionToJokeAPI', side_effect=[200, 404, 500, 403])
def test_connection(ConnectionToJokeAPI):
        assert ConnectionToJokeAPI() == 200
        assert ConnectionToJokeAPI() == 404
        assert ConnectionToJokeAPI() == 500
        assert ConnectionToJokeAPI() == 403