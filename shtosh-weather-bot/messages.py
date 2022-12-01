from typing import Optional
from dataclasses import dataclass
from api_service import get_weather


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def weather(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about the temperature and weather description"""
    wthr = get_weather(coordinates)
    countries_which_use_fahrenheit = ('KY', 'LR', 'US', )
    if wthr.country in countries_which_use_fahrenheit:
        return f'{wthr.location}, {wthr.description}\n' \
           f'Temperature is {wthr.temperature_fah}°F, feels like {wthr.temperature_fah_feeling}°F'
    else:
        return f'{wthr.location}, {wthr.description}\n' \
               f'Temperature is {wthr.temperature_cel}°C, feels like {wthr.temperature_cel_feeling}°C'


def wind(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about wind direction and speed"""
    wthr = get_weather(coordinates)
    countries_which_use_mph = ('AG', 'BS', 'GI', 'GD', 'GU', 'LR', 'MM', 'PR', 'SH',
                               'KN', 'LC', 'VC', 'WS', 'GB', 'US', 'VG', 'VI',)
    if wthr.country in countries_which_use_mph:
        return f'{wthr.wind_direction} wind {wthr.wind_speed_mph} mph'
    else:
        return f'{wthr.wind_direction} wind {wthr.wind_speed} m/s'


def suntime(coordinates: Optional[Coordinates] = None) -> str:
    """Returns a message about the time of sunrise and sunset"""
    wthr = get_weather(coordinates)
    countries_which_use_12_hour_clock = ('AU', 'BD', 'CA', 'CO', 'EG', 'SV', 'HN', 'IN', 'IE',
                                         'JO', 'MY', 'MX', 'NZ', 'NI', 'PK', 'PH', 'SA', 'US')
    if wthr.country in countries_which_use_12_hour_clock:
        return f'Sunrise: {wthr.sunrise.strftime("%-I:%M %p")}\n' \
               f'Sunset: {wthr.sunset.strftime("%-I:%M %p")}\n'
    else:
        return f'Sunrise: {wthr.sunrise.strftime("%H:%M")}\n' \
               f'Sunset: {wthr.sunset.strftime("%H:%M")}\n'
