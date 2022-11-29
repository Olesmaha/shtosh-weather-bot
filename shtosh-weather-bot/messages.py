from typing import Optional

from coordinates import get_coordinates, Coordinates
from api_service import get_weather


def weather(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about the temperature and weather description"""
    location_text = 'user'
    if coordinates is None:
        location_text = 'server'
        coordinates = get_coordinates()

    wthr = get_weather(coordinates)
    return f'{wthr.location}, {wthr.description} ({location_text})\n' \
           f'Temperature is {wthr.temperature}°C, feels like {wthr.temperature_feeling}°C'


def wind(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about wind direction and speed"""
    location_text = 'user'
    if coordinates is None:
        location_text = 'server'
        coordinates = get_coordinates()

    wthr = get_weather(coordinates)
    return f'{wthr.wind_direction} wind {wthr.wind_speed} m/s  ({location_text})'


def suntime(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about the time of sunrise and sunset"""
    location_text = 'user'
    if coordinates is None:
        location_text = 'server'
        coordinates = get_coordinates()

    wthr = get_weather(coordinates)
    return f'Sunrise: {wthr.sunrise.strftime("%H:%M")}\n' \
           f'Sunset: {wthr.sunset.strftime("%H:%M")}\n' \
           f' ({location_text})'
