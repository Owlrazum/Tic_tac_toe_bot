import asyncio
import logging
import board
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6538845135:AAGePgHV00Sclcn3LUhGM9K2dQ4lroYcQuY")
# Диспетчер
dp = Dispatcher()

kb = [
    [types.KeyboardButton(text="_ 0 0"), types.KeyboardButton(text="_ 0 1"), types.KeyboardButton(text="_ 0 2")],
    [types.KeyboardButton(text="_ 1 0"), types.KeyboardButton(text="_ 1 1"), types.KeyboardButton(text="_ 1 2")],
    [types.KeyboardButton(text="_ 2 0"), types.KeyboardButton(text="_ 2 1"), types.KeyboardButton(text="_ 2 2")]
]

element = 'x'


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите куда поставить крестик")

    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

@dp.message(F.text.startswith("_"))
async def empty(message: types.Message):
    global element, kb

    row = int(message.text[2])
    col = int(message.text[4])
    rowstr = message.text[2]
    colstr = message.text[4]
    board.board[row][col] = element
    el_text = "крестик" if element == 'x' else "нолик"
    kb[row][col] = types.KeyboardButton(text=element + " " + rowstr + " " + colstr)
    text = el_text + " поставлен в позицию " + rowstr + " " + colstr + "\n"
    text += "Выберите куда поставить " + ('нолик' if element == 'x' else 'крестик')
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите куда поставить " + el_text)
    element = 'o' if element == 'x' else 'x'
    await message.reply(text, reply_markup=keyboard)

@dp.message(F.text.startswith("x"))
async def cross(message: types.Message):
    el_text = "крестик" if element == 'x' else "нолик"  
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите куда поставить " + el_text)
    await message.reply("Поле занятно крестиком, выберете другое поле", reply_markup=keyboard)

@dp.message(F.text.startswith("o"))
async def noll(message: types.Message):
    el_text = "крестик" if element == 'x' else "нолик"
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите куда поставить " + el_text)
    await message.reply("Поле занятно крестиком, выберете другое поле", reply_markup=keyboard)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

