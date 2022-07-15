
from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Приветствую Вас! {message.from_user.full_name}")


@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo2 = open('media/tn2jcjcglxxx.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo2)


@dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

    question = "True к какому типу данных относяться?"
    answer = [
        'Int', 'Str', 'Bool', 'Нет такого типа'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Будь внимателен",
        explanation_parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup.add(button_call_2)

    question = "В честь какого животного назван самый распространненый язык программирования?"
    answer = [
        'Питон', 'Анаконда', 'Тигр'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Легко",
        explanation_parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def quiz_3(call: types.CallbackQuery):
    question = "Отвечай!!!"
    answer = [
        '55', '32', '36', '16', '44'
    ]
    photo = open("media/1.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Ошибочка",
        explanation_parse_mode=ParseMode.MARKDOWN
    )


@dp.message_handler()
async def echo(message: types.Message):
    a = message.text
    try:
        b = 1
        a = int(a)
    except:
        pass
        b = 0
    if b == 1:
        await bot.send_message(message.chat.id, f"{a ** 2}")
    elif b == 0:
        await bot.send_message(message.chat.id, a)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
