from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_LOCATION = InlineKeyboardButton('Send geolocation', request_location=True)
BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='weather')
BTN_WIND = InlineKeyboardButton('Wind', callback_data='wind')
BTN_SUN_TIME = InlineKeyboardButton('Sunrise and sunset', callback_data='sun_time')

LOCATION = InlineKeyboardMarkup().add(BTN_LOCATION)
START = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME)
WEATHER = InlineKeyboardMarkup().add(BTN_WIND, BTN_SUN_TIME)
WIND = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_SUN_TIME)
SUN_TIME = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND)
