import pytest
from joke_machine import error_handler

def test_error_handler_default():
    with pytest.raises(ValueError) as exc_info:
        testerror = error_handler('exception')
    assert str(exc_info.value) == 'exception'

@pytest.mark.parametrize("testdata, expected",[("test", "test"),("data", "data"),("program", "program")])
def test_error_handler(testdata,expected):
    with pytest.raises(ValueError) as exc_info:
        testerror = error_handler(testdata)
    assert str(exc_info.value) == expected

@pytest.mark.parametrize("testdata, expected",[("$%", "$%"),("&&&&", "&&&&"),("!@!!!", "!@!!!")])
def test_error_handler_sign_test(testdata,expected):
    with pytest.raises(ValueError) as exc_info:
        testerror = error_handler(testdata)
    assert str(exc_info.value) == expected
