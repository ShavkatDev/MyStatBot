from aiogram import Bot, Dispatcher, executor, types
from config import telegramToken
from aiogram.dispatcher.filters import Text

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import config
from aiogram.dispatcher import FSMContext

import getHtml
import takeInfo
import emoji

storage = MemoryStorage()
bot = Bot(token=telegramToken)
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    login = State()
    password = State()


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Ввести данные", "Статистика", "Хелп"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Даров это бот для MyStat!", reply_markup=keyboard)


@dp.message_handler(Text(equals="Ввести данные"))
async def user_register(message: types.Message):
    await message.answer("Введите логин")
    await UserState.login.set()


@dp.message_handler(state=UserState.login)
async def get_login(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Введите пароль")
    await UserState.password.set()


@dp.message_handler(state=UserState.password)
async def get_password(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    config.log_in(data["username"], data["password"])
    await state.finish()


@dp.message_handler(Text(equals="Статистика"))
async def statistic(message: types.Message):
    if config.login == False and config.password == False:
        await message.answer("Вы не ввели данные")
    else:
        msg = await message.answer("Загрузка...")
        try:
            getHtml.getHtml()
            printArr = takeInfo.main()
            await message.answer(f"{printArr[0]}\nМесто в группе - {printArr[1]}{emoji.emojize(':1st_place_medal:')}\n\nОчки - {printArr[2]}{emoji.emojize(':star:')}\nАлмазы - {printArr[3]}{emoji.emojize(':gem_stone:')}\nМонеты - {printArr[4]}{emoji.emojize(':money_bag:')}\nБэйджи - {printArr[5]}{emoji.emojize(':pound_banknote:')}")
            await msg.delete()
        except:
            await msg.delete()
            await message.answer("Неправильный логин или пароль!")
            return


@dp.message_handler(Text(equals="Хелп"))
async def helpToClient(message: types.Message):
    await message.answer("тут ничего нет :(")


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
