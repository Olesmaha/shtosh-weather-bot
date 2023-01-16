import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
import inline_keyboard
import messages
import config
from all_db_operations import put_user_data, get_coordinates, init_tables

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def show_weather(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Send geolocation', request_location=True))
    await message.answer(text=f"Hello, I'm weather bot. Please, send me your location.",
                         reply_markup=keyboard)


@dp.message_handler(content_types=ContentType.LOCATION)
async def get_location(message: types.Message):
    put_user_data(message.from_user.id,
                  message.from_user.first_name,
                  user_coordinates_latitude=message.location.latitude,
                  user_coordinate_longitude=message.location.longitude)
    await message.answer(text=f'Thank you, {message.from_user.first_name}! Now choose type of information:',
                         reply_markup=inline_keyboard.START)


@dp.message_handler(commands='weather')
async def show_weather(message: types.Message):
    await message.answer(text=messages.weather(
        get_coordinates(message.from_user.id)[0],
        get_coordinates(message.from_user.id)[1],
        message.from_user.id),
                         reply_markup=inline_keyboard.WEATHER)


@dp.message_handler(commands='wind')
async def show_wind(message: types.Message):
    await message.answer(text=messages.wind(
        get_coordinates(message.from_user.id)[0],
        get_coordinates(message.from_user.id)[1],
        message.from_user.id),
                         reply_markup=inline_keyboard.WIND)


@dp.message_handler(commands='sun_time')
async def show_sun_time(message: types.Message):
    await message.answer(text=messages.suntime(
        get_coordinates(message.from_user.id)[0],
        get_coordinates(message.from_user.id)[1],
        message.from_user.id),
                         reply_markup=inline_keyboard.SUN_TIME)


@dp.message_handler(commands='refresh')
async def refresh(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Refresh geolocation', request_location=True))
    await message.answer(text=f"Please, click the button.",
                         reply_markup=keyboard)


@dp.callback_query_handler(text='weather')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weather(
        get_coordinates(callback_query.from_user.id)[0],
        get_coordinates(callback_query.from_user.id)[1],
        callback_query.from_user.id),
        reply_markup=inline_keyboard.WEATHER)


@dp.callback_query_handler(text='wind')
async def process_callback_wind(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.wind(
        get_coordinates(callback_query.from_user.id)[0],
        get_coordinates(callback_query.from_user.id)[1],
        callback_query.from_user.id),
        reply_markup=inline_keyboard.WIND)


@dp.callback_query_handler(text='sun_time')
async def process_callback_sun_time(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.suntime(
        get_coordinates(callback_query.from_user.id)[0],
        get_coordinates(callback_query.from_user.id)[1],
        callback_query.from_user.id),
        reply_markup=inline_keyboard.SUN_TIME)


@dp.callback_query_handler(text='refresh')
async def process_callback_refresh(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Refresh geolocation', request_location=True))
    await bot.send_message(
        callback_query.from_user.id,
        text=f"Please, click the button.",
        reply_markup=keyboard)


if __name__ == '__main__':
    init_tables()
    executor.start_polling(dp, skip_updates=True)
