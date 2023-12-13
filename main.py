import sys
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, FSInputFile,
                           InlineKeyboardMarkup)
from aiogram.enums import ParseMode

##################################################################################################
API_TOKEN = "5587455597:AAETESl92cqEM_XkZ5h9AXXPt_6myvFnWz4"

# Текст сообщений
text_1 = "text-1"
text_2 = "text-2"
text_3 = "text-3"
text_4 = "text-4"

# наименование видео файлов
video_1_txt = 'video_1.mp4'  # НГ
video_2_txt = 'video_2.mp4'  # баба с фотиком
video_3_txt = 'video_3.mp4'  # лежит на мосту
video_4_txt = 'video_4.mp4'  # горы
video_5_txt = 'video_5.mp4'  #
video_6_txt = 'video_6.mp4'  #
video_7_txt = 'video_7.mp4'  #

# наименование аудио файлов
audio_1 = "audio_1.mp3"
audio_2 = "audio_2.mp3"

# текст кнопок
button_1_1 = "button_1_1"
button_1_2 = "button_1_2"
button_2_1 = "button_2_1"
button_2_2 = "button_2_2"
button_3_1 = "button_3_1"
button_3_2 = "button_3_2"
button_3_3 = "button_3_3"
button_3_4 = "button_3_4"
button_3_5 = "button_3_5"

# Задержка между отправкой сообщений
delay_1 = 1  # Сообщения
delay_2 = 5  # Видео

######################################################################################

dp = Dispatcher()

but_3_1 = KeyboardButton(text=button_3_1)
but_3_2 = KeyboardButton(text=button_3_2)
but_3_3 = KeyboardButton(text=button_3_3)
but_3_4 = KeyboardButton(text=button_3_4)
but_3_5 = KeyboardButton(text=button_3_5)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[[but_3_1], [but_3_2], [but_3_3], [but_3_4], [but_3_5]],
                               one_time_keyboard=True)

video_1 = FSInputFile(f"video_dir/{video_1_txt}", filename=video_1_txt)
video_2 = FSInputFile(f"video_dir/{video_2_txt}", filename=video_2_txt)

video_3 = FSInputFile(f"video_dir/{video_3_txt}", filename=video_3_txt)
video_4 = FSInputFile(f"video_dir/{video_4_txt}", filename=video_4_txt)
video_5 = FSInputFile(f"video_dir/{video_5_txt}", filename=video_5_txt)
video_6 = FSInputFile(f"video_dir/{video_6_txt}", filename=video_6_txt)
video_7 = FSInputFile(f"video_dir/{video_7_txt}", filename=video_7_txt)

but_list = [button_3_1, button_3_2, button_3_3, button_3_4, button_3_5]
vid_list = [video_3, video_4, video_5, video_6, video_7]

audio_1 = FSInputFile(f"audio_dir/{audio_1}", filename=audio_1)
audio_2 = FSInputFile(f"audio_dir/{audio_2}", filename=audio_2)


class Form(StatesGroup):
    block_1 = State()
    block_2 = State()
    block_3 = State()


@dp.message(CommandStart())
async def start_text(message: Message, state: FSMContext):
    logging.info("CommandStart")
    await state.set_state(Form.block_1)
    await message.answer(text=text_1)
    await asyncio.sleep(delay_1)
    try:
        await message.bot.send_video(message.chat.id, video=video_1)
    except Exception as ex:
        ex_txt = "Кто-то забыл добавить первое видео"
        await message.answer(ex_txt)
        logging.error(ex_txt, ex)

    await asyncio.sleep(delay_2)
    await message.answer(
        text=text_2,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=button_1_1), KeyboardButton(text=button_1_2)]],
            resize_keyboard=True)
    )


@dp.message(Form.block_1, F.text.contains(button_1_1))
async def go_to_video_1(message: Message, state: FSMContext):
    logging.info(message.text)
    await state.set_state(Form.block_3)

    try:
        await message.answer_video(video=video_2)
    except Exception as ex:
        ex_txt = "Кто-то забыл добавить второе видео"
        await message.answer(ex_txt)
        logging.error(ex_txt, ex)

    await asyncio.sleep(delay_2)

    await message.answer(text=text_3, reply_markup=keyboard)


@dp.message(Form.block_1, F.text.contains(button_1_2))
async def go_to_audio_choose(message: Message, state: FSMContext):
    logging.info(message.text)
    await state.set_state(Form.block_2)
    await message.answer(
        text='Выберите необходимый вариант',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=button_2_1), KeyboardButton(text=button_2_2)]],
            resize_keyboard=True,
            one_time_keyboard=True)
    )


@dp.message(Form.block_2, F.text.contains(button_2_1))
async def go_to_audio_1(message: Message, state: FSMContext):
    logging.info(message.text)
    await state.set_state(Form.block_3)
    try:
        await message.bot.send_audio(message.chat.id, audio=audio_1)
    except Exception as ex:
        ex_txt = "Кто-то забыл добавить audio_1"
        await message.answer(ex_txt)
        logging.error(ex_txt, ex)

    await message.answer(text=text_3, reply_markup=keyboard)


@dp.message(Form.block_2, F.text.contains(button_2_2))
async def go_to_audio_2(message: Message, state: FSMContext):
    logging.info(message.text)
    await state.set_state(Form.block_3)
    try:
        await message.bot.send_audio(message.chat.id, audio=audio_2)
    except Exception as ex:
        ex_txt = "Кто-то забыл добавить audio_2"
        await message.answer(ex_txt)
        logging.error(ex_txt, ex)

    await message.answer(text=text_3, reply_markup=keyboard)


@dp.message(Form.block_3)
async def go_to_video_3(message: Message, state: FSMContext):
    logging.info(message.text)
    await state.clear()
    m_text = message.text
    vid_i = but_list.index(m_text)
    vid_out = vid_list[vid_i]
    try:
        await message.answer_video(video=vid_out)
    except Exception as ex:
        ex_txt = f"Кто-то забыл добавить video_{vid_i + 3}"
        await message.answer(ex_txt)
        logging.error(ex_txt, ex)
    await asyncio.sleep(delay_2)
    await message.answer(text=text_4, reply_markup=ReplyKeyboardRemove())


@dp.message(Form.block_3, F.text.contains(button_3_2))
async def go_to_video_4(message: Message, state: FSMContext):
    logging.info(message.text)
    await state.clear()
    await message.answer_video(video=video_4)
    await asyncio.sleep(delay_2)
    await message.answer(text=text_4, reply_markup=ReplyKeyboardRemove())


@dp.message()
async def echo_handler(message: Message):
    await message.answer("Нажмите необходимую кнопку или введите команду /start")


async def main():
    # dp = Dispatcher()
    bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
