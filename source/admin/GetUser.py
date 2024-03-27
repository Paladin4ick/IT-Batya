import aiogram
from aiogram.types import Message
from aiogram.filters import Command

router = aiogram.Router()

@router.message(Command(commands=["user"]))
async def get_user(message: Message):
    message_content = message.text[5:]
    user = message.from_user
    message_text = (f"""
**Имя: ** `{user.first_name}` ```python message.from_user.first_name```
**Фамилия: **`{user.last_name}` ```python message.from_user.last_name```
**Имя и Фамилия: **`{user.full_name}` ```python message.from_user.full_name```
**Язык: **`{user.language_code}` ```python message.from_user.language_code```
**ID: **`{user.id}` ```python message.from_user.id```
**Ссылка: **`{user.url}` ```python message.from_user.url```
**Username: **`{user.username}` ```python message.from_user.username```
**Является ли пользователь ботом: **`{user.is_bot}` ```python message.from_user.is_bot```
**Есть ли у пользователя премиум: **`{user.is_premium}` ```python message.from_user.is_premium```
""")
    photos = await message.from_user.get_profile_photos()
    
    await message.answer(parse_mode="MarkdownV2", text=message_text)