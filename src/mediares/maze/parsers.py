"""Parse data from TVMaze."""

import logging
import typing

import dateutil.tz
import pycountry

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def parse_country(data: typing.Mapping) -> typing.Mapping:
    """Parse a TVMaze country.

    :param data: Country data from TVMaze
    :return: A mapping contain country and timezone data
    """
    timezone = dateutil.tz.gettz(data['timezone'])
    by_name = pycountry.countries.get(name=data['name'])
    return {
        'country': by_name,
        'timezone': timezone,
    }
