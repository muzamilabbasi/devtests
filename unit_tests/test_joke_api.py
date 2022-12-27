import pytest
from joke_machine import get_joke_api
from unittest.mock import MagicMock, patch
from unittest import mock


@mock.patch('joke_machine.get_joke_api', return_value='www.fake.com')
def test_getJokeApi_Url_found(getJokeApi):
    assert getJokeApi() == "www.fake.com"
    
@mock.patch('joke_machine.get_joke_api', side_effect=ValueError("404 not found"))
def test_getJokeApi_Url_notFound(getJokeApi):
    with pytest.raises(ValueError, match="404 not found"):
        getJokeApi()

@mock.patch('joke_machine.get_joke_api', return_value=200)
def test_getJokeApi_ret_val(getJokeApi):
    assert getJokeApi() == 200
    
@mock.patch('joke_machine.get_joke_api', side_effect=[200, 404])
def test_getJokeApi_ret_vals(getJokeApi):
    assert getJokeApi() == 200
    assert getJokeApi() == 404
    
def test_getJokeApi_res(getJokeApi):
    assert getJokeApi.status_code == 200