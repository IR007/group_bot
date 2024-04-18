from aiogram import types
from aiogram.enums import ContentType

from data.config import ADMINS
from filters import GroupFilter
from loader import dp, bot


@dp.message(lambda message: message.content_type == ContentType.NEW_CHAT_MEMBERS)
async def welcome_member(msg: types.Message):
    member_info = '\n'.join([f"Salom {user.mention_html(user.full_name)}, guruhga xush kelibsiz!" for user in msg.new_chat_members])
    await msg.reply(member_info)


@dp.message(lambda msg: msg.content_type == ContentType.LEFT_CHAT_MEMBER)
async def left_member(msg: types.Message):
    member = msg.left_chat_member
    if msg.from_user.id == member.id:
        await msg.answer(f"{member.mention_html(member.full_name)} foydalanuvchi guruhni tark etdi!")
    elif str(msg.from_user.id) in ADMINS:
        await msg.answer(f"{member.mention_html(member.full_name)} foydalanuvchi chopildi!")
