import logging
from aiogram import Bot, Dispatcher

API_TOKEN = '5732267504:AAF-QhCUqkM0sPqfpt62L9k3jFFX2M9sgW4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)