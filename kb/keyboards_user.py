from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton('help')
b2 = KeyboardButton('Запись')
b3 = KeyboardButton('Контактные данные')
# b3 = KeyboardButton('XYI', request_contact=True)
# b4 = KeyboardButton('pizda', request_location=True)


kb_user = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_user.row(b1,b2,b3)
