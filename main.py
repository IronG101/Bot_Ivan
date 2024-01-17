import sys
import os
from dotenv import load_dotenv
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
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN") # токен храним в файле .env см. README

# Текст сообщений
text_1 = "11"
text_2 = "Вы можете начать знакомство с телесной психологией через тело, выбрав практику либо через психику, выбрав медитацию"
text_3 = "5 сфер жизни"
text_4 = "Хотите больше погрузиться в личную трансформацию и встать на путь самоисцеления, приглашаю тебя в свой закрытый телеграм канал Пространство Ксении Кошкиной"

# наименование видео файлов
video_1_txt = 'video_1.mp4'  # Приветствие
video_2_txt = 'video_2.mp4'  # Ключ
video_3_txt = 'video_3.mp4'  # Личные границы Масштаб личности
video_4_txt = 'video_4.mp4'  # Самоценность Я есть
video_5_txt = 'video_5.mp4'  # Агрессия Не хочу не буду
video_6_txt = 'video_6.mp4'  # Предназначение Да будет так
video_7_txt = 'video_7.mp4'  # Сексуальность Хождение с хвостом

# наименование аудио файлов
audio_1 = "audio_1.m4a"      # медитация мама
audio_2 = "audio_2.m4a"      # медитация папа

# текст кнопок
button_1_1 = "Практика от стресса"
button_1_2 = "Медитация"
button_2_1 = "на маму"
button_2_2 = "на папу"
button_3_1 = "Личные границы"
button_3_2 = "Самоценность"
button_3_3 = "Агрессия, гнев"
button_3_4 = "Предназначение"
button_3_5 = "Сексуальность"

# Задержка между отправкой сообщений
delay_1 = 1  # Сообщения
delay_2 = 1  # Видео

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
