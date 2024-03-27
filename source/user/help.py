"""Импорт api"""
import aiogram
from aiogram.filters import Command
from aiogram.types import Message

router = aiogram.Router()

@router.message(Command(commands=["help"]))
async def helpcommand(message: Message):
    await message.answer(f"Привет, я <b>IT Батя</b> - бот помошник для начинющих и не только <b>IT специалистов</b>")



