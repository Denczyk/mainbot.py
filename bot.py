from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5052103879:AAG41eBQTpkOYaw29oOYd6GG0qQacdZeRZQ'

host = 'localhost'
user = 'root'
password = 'pu59bhuj00'
db_name = 'new'

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())