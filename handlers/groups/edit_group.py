import io

from aiogram import types
from aiogram.filters import Command

from filters import GroupFilter, AdminFilter
from loader import dp, bot


@dp.message(GroupFilter(), Command("set_photo", prefix="!/"))
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    # photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    #1-usul
    await message.chat.set_photo(photo=input_file)


@dp.message(GroupFilter(), Command("set_title"))
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    #2-usul
    await bot.set_chat_title(message.chat.id, title=title)


@dp.message(GroupFilter(), Command("set_description", prefix="!/"))
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    # 1-usul
    await bot.set_chat_description(message.chat.id, description=description)
    # 2-usul
    await message.chat.set_description(description=description)
