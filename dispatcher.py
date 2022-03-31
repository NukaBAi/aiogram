from main import bot, dp

from aiogram.types import Message
from config import id

async def send_to_admin(dp):
    await bot.send_message(chat_id = id, text = 'Hi, Boys\nWhere are you from?')


@dp.message_handler()
async def echo(message:Message):
    # if message.text == "nuka":
    #     text = f"Salem, sen tochno '{message.text}' degendi jazgyn keldi ma?"
    #     await bot.send_message(chat_id=message.from_user.id, text = text)
    if message.text == "pubg or fortnite":
        text = f"pubg"
        await bot.send_message(chat_id=message.from_user.id, text=text)
    elif message.text == "qalaisyn?":
        txt = f"Jaqsy ozin"
        await bot.send_message(chat_id=message.from_user.id, text=txt)
    elif message.text == "jaqsy":
        tt = f"Ote keremet!"
        await bot.send_message(chat_id=message.from_user.id, text=tt)

