import bot
import statefile
from database import *
from statefile import *
from keyboards import *

db = data_base('DATABASE.db')
db_add_user = add_new_user('DATABASE.db')
statefile.register_handlers_admin(dp)
statefile.register_handlers_admin2(dp)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Привіт!👋🇺🇦', reply_markup=Main)
    id_user = message.from_user.id
    db_add_user.start_user(id_user)


@dp.callback_query_handler(text='start_go', state=None)
async def poc_callback_but(message: types.Message):
    await bot.send_message(message.from_user.id, "🇺🇦Введи пароль:🇺🇦", reply_markup=slawa_)
    await States_p.STATE_GET_KEY.set()


@dp.callback_query_handler(text='add_time', state=None)
async def poc_callback_but(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, '🇺🇦Зараз напиши час, в який я маю тобі нагадувати розклад на завтра🔊🇺🇦', reply_markup=all_states)
    await States_add_time.STATE_GET_TIME.set()


@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.text == 'see':
        await db.find_Monday(message)
        await db.find_Tuesday(message)
        await db.find_Wednesday(message)
        await db.find_Thursday(message)
        await db.find_Friday(message)
        await db.find_Saturday(message)
        await db.find_Sunday(message)

    elif message.text == 'Go🇺🇦':
        await bot.send_message(message.from_user.id, 'Привіт!👋 Це твій електронний розклад занять!'
                                                     ' \nДостатньо заповнити поля та встановити час наповнення'
                                                     'і можна забути про старизну в виді папірців та ручок!🇺🇦🤘',
                               reply_markup=inline_start)


    elif message.text == 'Змінити час напомнення🕒🇺🇦':
        pass

    elif message.text == '❌Cancel🇺🇦':
        await bot.send_message(message.chat.id, 'Слава Україні!🇺🇦🇺🇦🇺🇦', reply_markup=Main)

executor.start_polling(dp, skip_updates=True)