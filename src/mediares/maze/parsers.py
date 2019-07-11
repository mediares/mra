"""Parse data from TVMaze."""

import logging
import typing

import dateutil.tz
import pycountry

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def parse_country(
        data: typing.Mapping,
        strict: bool = False,
) -> typing.Mapping:
    """Parse a TVMaze country.

    :param data: Country data from TVMaze
    :param strict: Raise ValueError if country is ambiguous
    :return: A mapping contain country and timezone data
    """
    timezone = dateutil.tz.gettz(data['timezone'])

    name = data['name']
    code = data['code']

    by_name = pycountry.countries.get(name=name)
    log.debug(f'name {name!r} parses as: {by_name}')

    if strict or by_name is None:
        by_code = pycountry.countries.get(alpha_2=code)
        log.debug(f'code {code!r} parses as: {by_code}')
    else:
        by_code = None

    if strict and by_name != by_code:
        raise ValueError(f'Ambiguous country')

    return {
        'country': by_name or by_code,
        'timezone': timezone,
    }
