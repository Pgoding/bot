from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from config import bot, dp
from kb import keyboards_user



# setting user


async def start_help(message : types.Message):
	await bot.send_message(message.from_user.id, 'Здараствуй меня зовут faza я пока что тестовый бот', reply_markup=keyboards_user.kb_user)


async def contact(message : types.Message):
	await bot.send_message(message.from_user.id, 'Мои контакты #######')
	await bot.send_sticker(message.from_user.id, sticker=('CAACAgIAAxkBAAEFAa5ipgjhZ8hwbRszAflrd6CLnGWUvQACBQADwDZPE_lqX5qCa011JAQ'))



# state machine

class FSMuser(StatesGroup):
	photo = State()
	name  = State()
	description = State()
	data = State()


# start
async def start_FSM(message : types.Message):
	await FSMuser.photo.set()
	await message.reply('Загрузи фото')
# one
async def load_photo(message : types.Message, state : FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await FSMuser.next()
	await message.reply('Напиши имя')
# two
async def load_name(message : types.Message, state : FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMuser.next()
	await message.reply('Опиши')
# three
async def load_description(message : types.Message, state : FSMContext):
	async with state.proxy() as data:
		data['description'] = message.text
	await FSMuser.next()
	await message.reply('Назначть дату')
# four
async def load_data(message : types.Message, state : FSMContext):
	async with state.proxy() as data:
		data['load_data'] = message.text

	async with state.proxy() as data:
		await message.reply(str(data))

	await state.finish()

# exit
async def exite(message : types.Message, state : FSMContext):
	current_state = await state.get_state()

	if current_state is None:
		return

	await state.finish()
	await message.reply('пока')












def register_hendler(dp : Dispatcher):
	dp.register_message_handler(start_help, commands=['start','help'])
	dp.register_message_handler(contact, Text(equals='Контактные данные', ignore_case=True, ))
	dp.register_message_handler(start_FSM, Text(equals='Запись', ignore_case=True, ), state=None)
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMuser.photo )
	dp.register_message_handler(load_name, state=FSMuser.name )
	dp.register_message_handler(load_description, state=FSMuser.description)
	dp.register_message_handler(load_data, state=FSMuser.data)
	dp.register_message_handler(exite, state='*', commands='отмена')
	dp.register_message_handler(exite, Text(equals='отмена', ignore_case=True), state='*')