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

    by_name = pycountry.countries.lookup(name)
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


def parse_network(
        data: typing.Mapping,
) -> typing.Mapping:
    """Parse a TVMaze network.

    :param data: Network data from TVMaze
    :return: A mapping contain country and timezone data
    """
    return {
        'maze_id': data['id'],
        'name': data['name'],
        **parse_country(data['country']),
    }


def parse_webchannel(
        data: typing.Mapping,
) -> typing.Mapping:
    """Parse a TVMaze Web Channel.

    :param data: Web Channel data from TVMaze
    :return: A mapping contain country and timezone data
    """
    country_data = data['country']
    if country_data:
        country = parse_country(country_data)
    else:
        country = {
            'country': None,
            'timezone': None,
        }
    return {
        'maze_id': data['id'],
        'name': data['name'],
        **country,
    }
