from datetime import datetime

from api_service import get_weather
from all_db_operations import get_weather_data


def weather(latitude, longitude, user_id) -> str:
    """Returns a message about the temperature and weather description"""
    get_weather(latitude, longitude, user_id)
    countries_which_use_fahrenheit = ('KY', 'LR', 'US', )
    wthr = get_weather_data(user_id)
    if wthr[-1] in countries_which_use_fahrenheit:
        return f'{wthr[1]}, {wthr[6]}\n' \
           f'Temperature is {wthr[4]}°F, feels like {wthr[5]}°F'
    else:
        return f'{wthr[1]}, {wthr[6]}\n' \
               f'Temperature is {wthr[2]}°C, feels like {wthr[3]}°C'


def wind(latitude, longitude, user_id) -> str:
    """Returns a message about wind direction and speed"""
    get_weather(latitude, longitude, user_id)
    countries_which_use_mph = ('AG', 'BS', 'GI', 'GD', 'GU', 'LR', 'MM', 'PR', 'SH',
                               'KN', 'LC', 'VC', 'WS', 'GB', 'US', 'VG', 'VI',)
    wthr = get_weather_data(user_id)
    if wthr[-1] in countries_which_use_mph:
        return f'{wthr[-2]} wind {wthr[-3]} mph'
    else:
        return f'{wthr[-2]} wind {wthr[-4]} m/s'


def suntime(latitude, longitude, user_id) -> str:
    """Returns a message about the time of sunrise and sunset"""
    get_weather(latitude, longitude, user_id)
    countries_which_use_12_hour_clock = ('AU', 'BD', 'CA', 'CO', 'EG', 'SV', 'HN', 'IN', 'IE',
                                         'JO', 'MY', 'MX', 'NZ', 'NI', 'PK', 'PH', 'SA', 'US')
    wthr = get_weather_data(user_id)
    frmt = "%Y-%m-%d %H:%M:%S"
    sunrise = datetime.strptime(wthr[-6], frmt)
    sunset = datetime.strptime(wthr[-5], frmt)
    if wthr[-1] in countries_which_use_12_hour_clock:
        return f'Sunrise: {sunrise.strftime("%-I:%M %p")}\n' \
               f'Sunset: {sunset.strftime("%-I:%M %p")}\n'
    else:
        return f'Sunrise: {sunrise.strftime("%H:%M")}\n' \
               f'Sunset: {sunset.strftime("%H:%M")}\n'
