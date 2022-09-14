from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from config import *
from hendlers import other, user, admin


async def on_startup(_):
    print('bot_on')


def main():
    user.register_hendler(dp)
    # other.register_hendler(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    main()