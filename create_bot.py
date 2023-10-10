from aiogram import Bot
from aiogram.dispatcher import Dispatcher 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from secret import token, service_key_vk
# from DB.database import Datebase

BOT_TOKEN = token
SERVICE_KEY = service_key_vk

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage()) 

# db_clients = Datebase('DB/clients.db')

vers = '5.131'
url = 'https://vk.com/id'
url_group = 'https://vk.com/'