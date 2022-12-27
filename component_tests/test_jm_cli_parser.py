import pytest
from unittest.mock import MagicMock, patch
from unittest import mock
from joke_machine import argument_parser

def test_argument_parser_default():
    parser = argument_parser()
    assert parser.number_of_jokes == 1

@mock.patch('joke_machine.argument_parser', side_effect=[3, 5, 10])
def test_argument_parser(argument_parser):
    assert argument_parser() == 3
    assert argument_parser() == 5
    assert argument_parser() == 10