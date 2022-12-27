import pytest
from joke_machine import get_joke
from unittest.mock import MagicMock, patch
from unittest import mock

@mock.patch('joke_machine.get_joke', side_effect=ValueError("No Joke Found"))
def test_getJoke_no_joke(getJoke):
    with pytest.raises(ValueError, match="No Joke Found"):
        getJoke()

@mock.patch('joke_machine.get_joke', side_effect=ValueError("Error: An invalid type was supplied"))
def test_getJoke_invalid_joke(getJoke):
    with pytest.raises(ValueError, match="Error: An invalid type was supplied"):
        getJoke()

@mock.patch('joke_machine.get_joke', side_effect=["singleJoke", "twopart\ntwopart", "multilinejoke\nmultilinejoke\nmultilinejoke"])
def test_getJokeType_ret_jokes(getJoke):
    assert getJoke() == "singleJoke"
    assert getJoke() == "twopart\ntwopart"
    assert getJoke() == "multilinejoke\nmultilinejoke\nmultilinejoke"  

def test_getJokeType_ret_jokes(getJoke):
    assert getJoke != ""