import pytest
from joke_machine import get_joke_api, get_joke_type, get_joke, joke_machine_runner

@pytest.fixture
def getJokeApi():
    getResponse = get_joke_api()
    return getResponse

@pytest.fixture
def getJokeType(getJokeApi):
    getResponse = get_joke_type(getJokeApi)
    return getResponse

@pytest.fixture
def getJoke(getJokeApi, getJokeType):
    getResponse = get_joke(getJokeApi, getJokeType)
    return getResponse

@pytest.fixture
def getJokeRunner():
    return joke_machine_runner
