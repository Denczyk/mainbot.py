from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import *
from keyboards import *
from database import *

db = add_plan_to_db('DATABASE.db')

class States_p(StatesGroup):
    STATE_GET_KEY = State()
    STATE_MONDAY = State()
    STATE_TUESDAY = State()
    STATE_WEDNESDAY = State()
    STATE_THURSDAY = State()
    STATE_FRIDAY = State()
    STATE_SATURDAY = State()
    STATE_SUNDAY = State()


@dp.message_handler(commands=['Почати!👣🇺🇦'], state=None)
async def cm_start(message: types.Message):
    await States_p.STATE_GET_KEY.set()
    await bot.send_message(message.chat.id, '🇺🇦➡Пароль⬅🇺🇦', reply_markup=inline_start)


@dp.message_handler(content_types=['text'], state=States_p.STATE_GET_KEY)
async def get_key(message: types.Message, state: FSMContext):

    if message.text == 'Слава Україні!🇺🇦':
        await States_p.next()
        await bot.send_message(message.chat.id, '🇺🇦➡Понеділок⬅:🇺🇦', reply_markup=all_states)

    else:
        await bot.send_message(message.from_user.id, 'В доступі відмовлено!🇺🇦')
        await States_p.finish()

@dp.message_handler(content_types=['text'], state=States_p.STATE_MONDAY)
async def get_monday(message: types.Message, state: FSMContext):

    if message.text == '❌Cancel🇺🇦':
        await state.finish()
        await message.reply('OK❕', reply_markup=Main)

    elif message.text == '⚠Пропустити🇺🇦':
        await bot.send_message(message.chat.id, 'Йдемо далі!🇺🇦')
        await bot.send_message(message.chat.id, "🇺🇦➡Вівторок⬅:🇺🇦")
        await States_p.STATE_TUESDAY.set()

    else:
        data_para = message.text
        id_user = message.from_user.id
        db.add_monday(data_para, id_user)
        await bot.send_message(message.chat.id, '🇺🇦➡Вівторок⬅:🇺🇦')
        await States_p.next()


@dp.message_handler(state=States_p.STATE_TUESDAY)
async def get_tuesday(message: types.Message, state: FSMContext):

    if message.text == '❌Cancel🇺🇦':
        await state.finish()
        await message.reply('OK❕🇺🇦', reply_markup=Main)

    elif message.text == '⚠Пропустити🇺🇦':
        await bot.send_message(message.chat.id, 'Йдемо далі!🇺🇦')
        await bot.send_message(message.chat.id, "🇺🇦➡Середа⬅:🇺🇦")
        await States_p.STATE_WEDNESDAY.set()

    else:
        data_para = message.text
        id_user = message.from_user.id
        db.add_tuesday(data_para, id_user)
        await States_p.next()
        await bot.send_message(message.chat.id, '🇺🇦➡Середа⬅:🇺🇦')


@dp.message_handler(state=States_p.STATE_WEDNESDAY)
async def get_wednesday(message: types.Message, state: FSMContext):

    if message.text == '❌Cancel🇺🇦':
        await state.finish()
        await message.reply('OK❕🇺🇦', reply_markup=Main)

    elif message.text == '⚠Пропустити🇺🇦':
        await bot.send_message(message.chat.id, 'Йдемо далі!🇺🇦')
        await bot.send_message(message.chat.id, "🇺🇦➡Четвер⬅:🇺🇦")
        await States_p.STATE_THURSDAY.set()

    else:
        data_para = message.text
        id_user = message.from_user.id
        db.add_wednesday(data_para, id_user)
        await States_p.next()
        await bot.send_message(message.chat.id, '🇺🇦➡Четвер⬅:🇺🇦')


@dp.message_handler(state=States_p.STATE_THURSDAY)
async def get_thursday(message: types.Message, state: FSMContext):

    if message.text == '❌Cancel🇺🇦':
        await state.finish()
        await message.reply('OK❕🇺🇦', reply_markup=Main)

    elif message.text == '⚠Пропустити🇺🇦':
        await bot.send_message(message.chat.id, 'Йдемо далі!🇺🇦')
        await bot.send_message(message.chat.id, "🇺🇦➡П'ятниця⬅:🇺🇦")
        await States_p.STATE_FRIDAY.set()

    else:
        data_para = message.text
        id_user = message.from_user.id
        db.add_thursday(data_para, id_user)
        await States_p.next()
        await bot.send_message(message.chat.id, "🇺🇦➡П'ятниця⬅:🇺🇦")


@dp.message_handler(state=States_p.STATE_FRIDAY)
async def get_friday(message: types.Message, state: FSMContext):

    if message.text == '❌Cancel🇺🇦':
        await state.finish()
        await message.reply('OK❕🇺🇦', reply_markup=Main)

    elif message.text == '⚠Пропустити🇺🇦':
        await bot.send_message(message.chat.id, 'Йдемо далі!🇺🇦')
        await bot.send_message(message.chat.id, "🇺🇦➡Субота⬅:🇺🇦")
        await States_p.STATE_SATURDAY.set()

    else:
        data_para = message.text
        id_user = message.from_user.id
        db.add_friday(data_para, id_user)
        await States_p.next()
        await bot.send_message(message.chat.id, '🇺🇦➡Субота⬅:🇺🇦')


@dp.message_handler(state=States_p.STATE_SATURDAY)
async def get_saturday(message: types.Message, state: FSMContext):

    if message.text == '❌Cancel🇺🇦':
        await state.finish()
        await message.reply('OK❕🇺🇦', reply_markup=Main)

    elif message.text == '⚠Пропустити🇺🇦':
        await bot.send_message(message.chat.id, 'Йдемо далі!🇺🇦')
        await bot.send_message(message.chat.id, "🇺🇦➡Неділя⬅:🇺🇦")
        await States_p.STATE_SUNDAY.set()

    else:
        data_para = message.text
        id_user = message.from_user.id
        db.add_saturday(data_para, id_user)
        await States_p.next()
        await bot.send_message(message.chat.id, '🇺🇦➡Неділя⬅:🇺🇦')


@dp.message_handler(state=States_p.STATE_SUNDAY)
async def get_sunday(message: types.Message, state: FSMContext):
    id_user = message.from_user.id
    data_para = message.text
    db.add_sunday(data_para, id_user)

    await state.finish()
    await message.reply('Записано!☑🇺🇦', reply_markup=Main)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='Почати!👣', state=None)
    dp.register_message_handler(get_key, content_types=['text'], state=States_p.STATE_GET_KEY)
    dp.register_message_handler(get_monday, content_types=['text'], state=States_p.STATE_MONDAY)
    dp.register_message_handler(get_tuesday, content_types=['text'], state=States_p.STATE_TUESDAY)
    dp.register_message_handler(get_wednesday, content_types=['text'], state=States_p.STATE_WEDNESDAY)
    dp.register_message_handler(get_thursday, content_types=['text'], state=States_p.STATE_THURSDAY)
    dp.register_message_handler(get_friday, content_types=['text'], state=States_p.STATE_FRIDAY)
    dp.register_message_handler(get_saturday, content_types=['text'], state=States_p.STATE_SATURDAY)
    dp.register_message_handler(get_sunday, content_types=['text'], state=States_p.STATE_SUNDAY)

db_time = add_new_user('DATABASE.db')
db_ti_me = find_time('DATABASE.db')

class States_add_time(StatesGroup):
    STATE_GET_TIME = State()


@dp.message_handler(commands=['Додати час напомнення🕒'], state=None)
async def cm_start_time(message: types.Message):
    await States_add_time.STATE_GET_TIME.set()
    await message.reply('🇺🇦Зараз напиши час, в який я маю тобі нагадувати розклад на завтра!🇺🇦', reply_markup=all_states)


@dp.message_handler(content_types=['text'], state=States_add_time.STATE_GET_TIME)
async def get_time(message: types.Message, state: FSMContext):

    if message.text == '❌Cancel🇺🇦':
        await state.finish()
        await message.reply('OK!🇺🇦', reply_markup=Main)

    else:
        id_user = message.from_user.id
        db_time.add_user(id_user, message.text)
        db_ti_me.give_time()

        await bot.send_message(message.chat.id, 'Зрозумів❕🇺🇦', reply_markup=Main)
        await state.finish()


def register_handlers_admin2(dp: Dispatcher):
    dp.register_message_handler(cm_start_time, commands='Додати час напомнення🕒🇺🇦', state=States_add_time.STATE_GET_TIME)
    dp.register_message_handler(get_time, content_types=['text'], state=States_add_time.STATE_GET_TIME)
