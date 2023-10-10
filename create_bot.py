from aiogram import Bot
from aiogram.dispatcher import Dispatcher 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from DB.database import Datebase

BOT_TOKEN = '5512199707:AAE7MzQfIU2gtM6Gkg2_RQfnju5S3W385R0'
SERVICE_KEY = 'f698fddbf698fddbf698fddb11f6e55dc5ff698f698fddb947f5587662c78409a9f6ffa'
# ID_TRASH_CHANNEL = '-1001500845075'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage()) 

# db_clients = Datebase('DB/clients.db')

vers = '5.131'
url = 'https://vk.com/id'
url_group = 'https://vk.com/'
# password = '1ArtemLebedevMolodec!'