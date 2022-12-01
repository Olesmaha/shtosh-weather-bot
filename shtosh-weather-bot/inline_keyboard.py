from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_LOCATION = InlineKeyboardButton('Send geolocation', request_location=True)
BTN_WEATHER_CEL = InlineKeyboardButton('Weather in Celsius', callback_data='weather_celsius')
BTN_WEATHER_KEL = InlineKeyboardButton('Weather in Kelvin', callback_data='weather_kelvin')
BTN_WIND = InlineKeyboardButton('Wind', callback_data='wind')
BTN_SUN_TIME = InlineKeyboardButton('Sunrise and sunset', callback_data='sun_time')

LOCATION = InlineKeyboardMarkup().add(BTN_LOCATION)
START = InlineKeyboardMarkup().add(BTN_WEATHER_CEL, BTN_WEATHER_KEL, BTN_WIND, BTN_SUN_TIME)
WEATHER_CEL = InlineKeyboardMarkup().add(BTN_WEATHER_KEL, BTN_WIND, BTN_SUN_TIME)
WEATHER_KEL = InlineKeyboardMarkup().add(BTN_WEATHER_CEL, BTN_WIND, BTN_SUN_TIME)
WIND = InlineKeyboardMarkup().add(BTN_WEATHER_CEL, BTN_WEATHER_KEL, BTN_SUN_TIME)
SUN_TIME = InlineKeyboardMarkup().add(BTN_WEATHER_CEL, BTN_WEATHER_KEL, BTN_WIND)
