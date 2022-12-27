import pytest
from joke_machine import joke_machine_runner
from unittest.mock import MagicMock, patch
from unittest import mock


@mock.patch('joke_machine.joke_machine_runner', return_value="I am a Joke")
def test_getJoke_no_joke(mock_runner):
        assert mock_runner() == "I am a Joke"

def test_getJoke_joke(getJokeRunner):
        assert getJokeRunner(1) != ""
    
@mock.patch('joke_machine.joke_machine_runner', side_effect=ValueError("Some Value Error"))
def test_getJokeType_raise_exception(mock_runner):
    with pytest.raises(ValueError, match="Some Value Error"):
        mock_runner()