from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_LOCATION = InlineKeyboardButton('Send geolocation', request_location=True)
BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='weather')
BTN_WIND = InlineKeyboardButton('Wind', callback_data='wind')
BTN_SUN_TIME = InlineKeyboardButton('Sunrise and sunset', callback_data='sun_time')
BTN_REFRESH = InlineKeyboardButton('Refresh coordinates', callback_data='refresh')

LOCATION = InlineKeyboardMarkup().add(BTN_LOCATION)
START = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_SUN_TIME)
WEATHER = InlineKeyboardMarkup().add(BTN_WIND, BTN_SUN_TIME, BTN_REFRESH)
WIND = InlineKeyboardMarkup().add(BTN_SUN_TIME, BTN_WEATHER, BTN_REFRESH)
SUN_TIME = InlineKeyboardMarkup().add(BTN_WEATHER, BTN_WIND, BTN_REFRESH)
