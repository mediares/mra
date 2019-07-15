import datetime

import pycountry.db
from pytest import param, mark

from mediares.maze import parsers


@mark.parametrize(
    'data', [
        param(
            {
                'id': 1,
                'name': 'NBC',
                'country': {
                    'name': 'United States',
                    'code': 'US',
                    'timezone': 'America/New_York',
                },
            },
        ),
    ],
)
def test_parse_network(data):
    expected_keys = {
        'maze_id',
        'name',
        'country',
        'timezone',
    }
    parsed = parsers.parse_network(data)
    assert not expected_keys.symmetric_difference(parsed.keys())
    assert isinstance(parsed['maze_id'], int)
    assert parsed['maze_id'] > 0
    assert isinstance(parsed['name'], str)
    assert parsed['name']
    assert isinstance(parsed['country'], pycountry.db.Data)
    assert isinstance(parsed['timezone'], datetime.tzinfo)


@mark.parametrize(
    'data', [
        param(
            {
                'id': 1,
                'name': 'Netflix',
                'country': None,
            },
        ),
        param(
            {
                'id': 2,
                'name': 'Hulu',
                'country': {
                    'name': 'United States',
                    'code': 'US',
                    'timezone': 'America/New_York',
                },
            },
        ),
    ],
)
def test_parse_webchannel(data):
    expected_keys = {
        'maze_id',
        'name',
        'country',
        'timezone',
    }
    parsed = parsers.parse_webchannel(data)
    assert not expected_keys.symmetric_difference(parsed.keys())
    assert isinstance(parsed['maze_id'], int)
    assert parsed['maze_id'] > 0
    assert isinstance(parsed['name'], str)
    assert parsed['name']
    if parsed['country'] or parsed['timezone']:
        assert isinstance(parsed['country'], pycountry.db.Data)
        assert isinstance(parsed['timezone'], datetime.tzinfo)
    else:
        assert parsed['country'] is None
        assert parsed['timezone'] is None
