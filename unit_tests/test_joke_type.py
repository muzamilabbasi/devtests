import pytest
from joke_machine import get_joke_type, get_joke_api
from unittest.mock import MagicMock, patch
from unittest import mock


@mock.patch('joke_machine.get_joke_type', side_effect=["single", "twopart"])
def test_getJokeType_ret_joke_type(getJokeType):
    assert getJokeType() == "single"
    assert getJokeType() == "twopart"
    
@mock.patch('joke_machine.get_joke_type', side_effect=ValueError("404 not found"))
def test_getJokeType_raise_exception(getJokeType):
    with pytest.raises(ValueError, match="404 not found"):
        getJokeType()

def test_getJokeType_ret_joke(getJokeType):
    assert getJokeType == "single" or getJokeType == "twopart"