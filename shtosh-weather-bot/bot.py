import logging
from typing import Optional
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType

import inline_keyboard
import messages
import config
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


users_date = {}
user_coordinates: Optional[Coordinates] = None


@dp.message_handler(commands='start')
async def show_weather(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Send geolocation', request_location=True))
    await message.answer(text=f"Hello, I'm weather bot. Please, send me your location.",
                         reply_markup=keyboard)


@dp.message_handler(content_types=ContentType.LOCATION)
async def get_location(message: types.Message):
    global user_coordinates
    user_coordinates = Coordinates(longitude=message.location.longitude, latitude=message.location.latitude)
    users_date[message.from_user.id] = user_coordinates
    await message.answer(text=f'Thank you! Now choose type of information:',
                         reply_markup=inline_keyboard.START)


@dp.message_handler(commands='weather_celsius')
async def show_weather(message: types.Message):
    await message.answer(text=messages.weather_celsius(users_date[message.from_user.id]),
                         reply_markup=inline_keyboard.WEATHER_CEL)


@dp.message_handler(commands='weather_kelvin')
async def show_weather(message: types.Message):
    await message.answer(text=messages.weather_kelvin(users_date[message.from_user.id]),
                         reply_markup=inline_keyboard.WEATHER_KEL)


@dp.message_handler(commands='wind')
async def show_wind(message: types.Message):
    await message.answer(text=messages.wind(users_date[message.from_user.id]),
                         reply_markup=inline_keyboard.WIND)


@dp.message_handler(commands='sun_time')
async def show_sun_time(message: types.Message):
    await message.answer(text=messages.suntime(users_date[message.from_user.id]),
                         reply_markup=inline_keyboard.SUN_TIME)


@dp.callback_query_handler(text='weather_celsius')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weather_celsius(users_date[callback_query.from_user.id]),
        reply_markup=inline_keyboard.WEATHER_CEL
    )


@dp.callback_query_handler(text='weather_kelvin')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weather_kelvin(users_date[callback_query.from_user.id]),
        reply_markup=inline_keyboard.WEATHER_KEL
    )


@dp.callback_query_handler(text='wind')
async def process_callback_wind(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.wind(users_date[callback_query.from_user.id]),
        reply_markup=inline_keyboard.WIND
    )


@dp.callback_query_handler(text='sun_time')
async def process_callback_sun_time(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.suntime(users_date[callback_query.from_user.id]),
        reply_markup=inline_keyboard.SUN_TIME
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
