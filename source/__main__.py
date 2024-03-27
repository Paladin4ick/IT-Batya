"""Importing required dependencies"""
import asyncio, aiogram, os, dotenv

from source.user import gpt, help, info

"""Import routers from the routers folder"""
from user import LessonCode
from admin import GetUser

"""Load an .env file from a private folder, the file contains private values for variables"""
dotenv.load_dotenv("./source/private/.env")

"""Bot launch function"""
async def main():

    """The bot variable to which we pass the token from the .env file"""
    client = aiogram.Bot(os.getenv("BOT_TOKEN"), parse_mode="HTML") 

    """The dispatcher variable through which interactions with the bot take place"""
    dispatcher = aiogram.Dispatcher()

    """Downloading routers from the routers folder"""
    dispatcher.include_routers(
        help.router,
        info.router,
        gpt.router,
        GetUser.router,
        LessonCode.router)

    """Deleting the webhook"""
    await client.delete_webhook(True)

    """Updating the bot when inactive"""
    await dispatcher.start_polling(client)

"""Launching the bot"""
if __name__ == "__main__":
    asyncio.run(main())
