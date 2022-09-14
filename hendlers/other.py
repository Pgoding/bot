# from aiogram import types
# from aiogram.dispatcher import Dispatcher
# from config import bot, dp 

# import json, string



# ХУЙНЯ
# async def  insult_filter(message : types.Message):
# 	if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
# 	.intersection(set(json.load(open('mate_data.json')))) != set():
# 		await message.reply('Маты запрещены')
# 		await message.delete()

# with open('mate_data.json') as f:
# 	for i in f:
# 		print(i)




# def register_hendler(dp : Dispatcher):
	# dp.register_message_handler(insult_filter)