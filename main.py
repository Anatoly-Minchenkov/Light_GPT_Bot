
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
from api_response import openai
from os import getenv

from database import orm

load_dotenv(find_dotenv())


bot = Bot(getenv('TELEGRAM_KEY'))

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    orm.add_user(message.from_user.id, message.from_user.first_name, message.from_user.username)
    text = f'Привет {message.from_user.first_name}! Я бот, который ответит на любые твои вопросы. Задай свой!'
    await message.bot.send_message(chat_id=message.from_user.id, text=text, )


@dp.message_handler()
async def handler_message(message: types.Message):
    # global count
    response = openai.get_response(message)
    try:
        orm.add_questions(message.text, response["choices"][0]["text"], message.from_user.username)
    except:
        await bot.send_message(chat_id=message.from_user.id, text=f'Сначала надо зарегистрироваться, прописав /start')
        return
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'{message.from_user.first_name}, {response["choices"][0]["text"]}')


if __name__ == '__main__':
    executor.start_polling(dp)
