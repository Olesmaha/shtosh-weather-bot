from urllib.request import urlopen
from dataclasses import dataclass
from datetime import tzinfo
import json
from zoneinfo import ZoneInfo


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """Returns current coordinates using IP address"""
    data = _get_ip_data()
    latitude = data['loc'].split(',')[0]
    longitude = data['loc'].split(',')[1]

    return Coordinates(latitude=latitude, longitude=longitude)


def _get_ip_data() -> dict:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    return json.loads(response)
