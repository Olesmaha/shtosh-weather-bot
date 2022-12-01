from typing import Optional
from dataclasses import dataclass
from api_service import get_weather


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def weather_celsius(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(coordinates)
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature_cel}°C, feels like {wthr.temperature_cel_feeling}°C'


def weather_kelvin(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(coordinates)
    return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature_kel}°K, feels like {wthr.temperature_kel_feeling}°K'


def wind(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about wind direction and speed"""
    wthr = get_weather(coordinates)
    return f'{wthr.wind_direction} wind {wthr.wind_speed} m/s'


def suntime(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about the time of sunrise and sunset"""
    wthr = get_weather(coordinates)
    return f'Sunrise: {wthr.sunrise.strftime("%c")}\n' \
           f'Sunset: {wthr.sunset.strftime("%c")}\n'
