import aiogram
from aiogram.filters import Command
from aiogram.types import Message
from g4f.client import Client
import g4f

router = aiogram.Router()

conversation_history = {}

def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history


@router.message(Command(commands=['clear']))
async def process_clear_command(message: Message):
    user_id = message.from_user.id
    conversation_history[user_id] = []
    await message.reply("История диалога очищена.")


@router.message(Command(commands=['gpt']))
async def send_welcome(message: Message):
    user_id = message.from_user.id
    user_input = message.text[4:]

    if user_id not in conversation_history:
        conversation_history[user_id] = []

    conversation_history[user_id].append({"role": "user", "content": user_input})
    conversation_history[user_id] = trim_history(conversation_history[user_id])

    chat_history = conversation_history[user_id]

    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=chat_history,
            provider=g4f.Provider.FreeGpt,
        )
        chat_gpt_response = response
    except Exception as e:
        print(f"{g4f.Provider.GeekGpt.__name__}:", e)
        chat_gpt_response = "Извините, произошла ошибка."

    conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})
    length = sum(len(message["content"]) for message in conversation_history[user_id])
    channel = message.message_thread_id
    if message.chat.id == -1002100184866:
        
        if channel == 16979:
            await message.answer(chat_gpt_response, parse_mode="Markdown")
        else:
            await message.reply("Вам временно ограничен доступ к боту", parse_mode="Markdown")
    else:
        await message.answer(chat_gpt_response, parse_mode="Markdown")