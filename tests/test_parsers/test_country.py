import datetime

import pycountry
from pytest import mark, param

from mediares.maze import parsers


@mark.parsing
@mark.parametrize(
    'data', [
        param(
            {
                'code': 'US',
                'name': 'United States',
                'timezone': 'America/New_York',
            },
            id='non-ambiguous',
        ),
        param(
            {
                'name': 'Czech Republic',
                'code': 'CZ',
                'timezone': 'Europe/Prague',
            },
            id='official_name',
        ),
        param(
            {
                'name': 'United States',
                'code': 'CZ',
                'timezone': 'Europe/Prague',
            },
            id='ambiguous',
        )
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


@mark.parsing
@mark.parametrize(
    'data', [
        param(
            {
                'code': 'US',
                'name': 'United States',
                'timezone': 'America/New_York',
            },
            id='non-ambiguous',
        ),
        param(
            {
                'name': 'Czech Republic',
                'code': 'CZ',
                'timezone': 'Europe/Prague',
            },
            id='official_name',
        ),
        param(
            {
                'name': 'United States',
                'code': 'CZ',
                'timezone': 'Europe/Prague',
            },
            id='ambiguous',
            marks=mark.xfail(
                raises=ValueError,
                reason='country is ambiguous',
            ),
        )
    ]
)
def test_parse_country_strict(data):
    expected_keys = {
        'country',
        'timezone',
    }
    parsed = parsers.parse_country(data, strict=True)
    assert not expected_keys.symmetric_difference(parsed.keys())
    assert isinstance(parsed['country'], pycountry.db.Data)
    assert isinstance(parsed['timezone'], datetime.tzinfo)
