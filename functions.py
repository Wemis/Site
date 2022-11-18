from aiogram import *

from aiogram.types import *


from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot("5590494171:AAFIwywnCO6_4dW0WkogqWCLSKp4aM-rcbo")
dp = Dispatcher(bot, storage=MemoryStorage())

inline_button1 = InlineKeyboardButton("See", callback_data="see")
button_see = InlineKeyboardMarkup(row_width=1)
button_see.add(inline_button1)


button_1 = KeyboardButton("1")
button_2 = KeyboardButton("2")

button_yes = KeyboardButton("yes")
button_menu = KeyboardButton("Menu 💗")
buttons2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons2.add(button_yes, button_menu)

buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons.add(button_1, button_2)



@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Please, press the button👇👇", reply_markup=kb.buttons_questionnaries)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)