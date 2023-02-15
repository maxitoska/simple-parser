import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

import json
from aiogram.utils.markdown import hbold, hlink
import time

from dotenv import load_dotenv

from parser import collect_data

load_dotenv()

bot = Bot(
    token=os.getenv("TOKEN"),
    parse_mode=types.ParseMode.HTML,
)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["🔪 Knives", "🧤 Gloves", "︻デ═一 Sniper Rifles"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Choose Category", reply_markup=keyboard)


@dp.message_handler(Text(equals="🔪 Knives"))
async def get_discount_knives(message: types.Message):
    await message.answer("Please waiting...")

    collect_data(cat_type=2)

    with open("result.json", encoding="utf8") as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = (
            f"{hlink(item.get('full_name'), item.get('steam_image'))}\n"
            f"{hbold('Discount: ')}{item.get('discount')}%\n"
            f"{hbold('Price: ')}${item.get('price')}🔥"
            f"{hbold('3D: ')}{item.get('3d')}"
        )

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


@dp.message_handler(Text(equals="🧤 Gloves"))
async def get_discount_gloves(message: types.Message):
    await message.answer("Please waiting...")

    collect_data(cat_type=13)

    with open("result.json", encoding="utf8") as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = (
            f"{hlink(item.get('full_name'), item.get('steam_image'))}\n"
            f"{hbold('Discount: ')}{item.get('discount')}%\n"
            f"{hbold('Price: ')}${item.get('price')}🔥"
            f"{hbold('3D: ')}{item.get('3d')}"
        )

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


@dp.message_handler(Text(equals="︻デ═一 Sniper Rifles"))
async def get_discount_sniper_rifles(message: types.Message):
    await message.answer("Please waiting...")

    collect_data(cat_type=4)

    with open("result.json", encoding="utf8") as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = (
            f"{hlink(item.get('full_name'), item.get('steam_image'))}\n"
            f"{hbold('Discount: ')}{item.get('discount')}%\n"
            f"{hbold('Price: ')}${item.get('price')}🔥"
            f"{hbold('3D: ')}{item.get('3d')}"
        )

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


executor.start_polling(dp)