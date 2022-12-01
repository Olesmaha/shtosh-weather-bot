from typing import Literal, TypeAlias
from urllib.request import urlopen
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
import json

from bot import Coordinates
import config

Celsius: TypeAlias = float
Fahrenheit: TypeAlias = float


class WindDirection(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315


@dataclass(slots=True, frozen=True)
class Weather:
    location: str
    temperature_cel: Celsius
    temperature_cel_feeling: Celsius
    temperature_fah: Fahrenheit
    temperature_fah_feeling: Fahrenheit
    description: str
    wind_speed: float
    wind_speed_mph: int
    wind_direction: str
    sunrise: datetime
    sunset: datetime
    country: str


def get_weather(coordinates=Coordinates) -> Weather:
    """Request the weather in OpenWeather API and returns it"""
    openweather_response = _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude
    )
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(latitude: float, longitude: float) -> str:
    url = config.CURRENT_WEATHER_API_CALL.format(latitude=latitude, longitude=longitude)
    return urlopen(url).read()


def _parse_openweather_response(openweather_response: str) -> Weather:
    openweather_dict = json.loads(openweather_response)
    return Weather(
        location=_parse_location(openweather_dict),
        temperature_cel=_parse_temperature_cel(openweather_dict),
        temperature_cel_feeling=_parse_temperature_cel_feeling(openweather_dict),
        temperature_fah=_parse_temperature_fah(openweather_dict),
        temperature_fah_feeling=_parse_temperature_fah_feeling(openweather_dict),
        description=_parse_description(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, 'sunrise'),
        sunset=_parse_sun_time(openweather_dict, 'sunset'),
        wind_speed=_parse_wind_speed(openweather_dict),
        wind_speed_mph=_parse_wind_speed_mph(openweather_dict),
        wind_direction=_parse_wind_direction(openweather_dict),
        country=_parse_country(openweather_dict)
    )


def _parse_location(openweather_dict: dict) -> str:
    return openweather_dict['name']


def _parse_temperature_cel(openweather_dict: dict) -> Celsius:
    return openweather_dict['main']['temp']


def _parse_temperature_cel_feeling(openweather_dict: dict) -> Celsius:
    return openweather_dict['main']['feels_like']


def _parse_temperature_fah(openweather_dict: dict) -> Fahrenheit:
    openweather_dict['main']['temp_fah'] = round((openweather_dict['main']['temp'] * 9 / 5) + 32, 1)
    return openweather_dict['main']['temp_fah']


def _parse_temperature_fah_feeling(openweather_dict: dict) -> Fahrenheit:
    openweather_dict['main']['fah_feels_like'] = round((openweather_dict['main']['feels_like'] * 9 / 5) + 32, 1)
    return openweather_dict['main']['fah_feels_like']


def _parse_description(openweather_dict) -> str:
    return str(openweather_dict['weather'][0]['description']).capitalize()


def _parse_sun_time(openweather_dict: dict, time: Literal['sunrise', 'sunset']) -> datetime:
    openweather_dict['sys'][time] = openweather_dict['sys'][time] + openweather_dict['timezone']
    return datetime.utcfromtimestamp(openweather_dict['sys'][time])


def _parse_wind_speed(openweather_dict: dict) -> float:
    return openweather_dict['wind']['speed']


def _parse_wind_speed_mph(openweather_dict: dict) -> int:
    openweather_dict['wind']['speed_mph'] = int(openweather_dict['wind']['speed'] * 2.23693629)
    return openweather_dict['wind']['speed_mph']


def _parse_wind_direction(openweather_dict: dict) -> str:
    degrees = openweather_dict['wind']['deg']
    degrees = round(degrees / 45) * 45
    if degrees == 360:
        degrees = 0
    return WindDirection(degrees).name


def _parse_country(openweather_dict: dict) -> str:
    return openweather_dict['sys']['country']
