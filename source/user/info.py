import aiogram
from aiogram.filters import Command
from aiogram.types import Message

router = aiogram.Router()

@router.message(Command(commands=["info"]))
async def info_command(message: Message):
    await message.answer("""
<b>ИНФОРМАЦИЯ О БАТЬКЕ</b>
<b>💻 Разработчик: </b>@si_paladin4ick
<b>⚙️ Версия:</b> <code>0.5</code>
<b>❇️ Статус:</b> <code>Активная разработка</code>
<b>🌍 Язык:</b> <code>Русский</code>
<b>🐍 Яп:</b> <code>Python</code>""")