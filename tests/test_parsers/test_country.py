import datetime

import pycountry
from pytest import mark, param

from mediares.maze import parsers

@mark.parsing
@mark.parametrize(
    'data', [
        {
            'code': 'US',
            'name': 'United States',
            'timezone': 'America/New_York',
        },
    ]
)
def test_parse_country(data):
    expected_keys = {
        'country',
        'timezone',
    }
    parsed = parsers.parse_country(data)
    assert not expected_keys.symmetric_difference(parsed.keys())
    assert isinstance(parsed['country'], pycountry.db.Data)
    assert isinstance(parsed['timezone'], datetime.tzinfo)
