# Телеграмм бот  aiogram 3.2.0
## !! Перед запуском 
1) (по желанию) Установить виртуальное окружение `python -m venv venv` 
2) Установить все необходимые библиотеки: `pip install -r requirements.txt`
___
### **Редактируются данные только с 12 по 43 строку!!!**





**Нужно создать папки `audio_dir` и `video_dir`**

Аудио файлы загружаются в папку `audio_dir`  
Аудио файлы должны быть в формате .MP3 или .M4A

Видео файлы загружаются в папку `video_dir`  
Видео файлы должны быть в формате MPEG4
---
**Есть возможность отправки аудио и видео через URL (без сохранения файлов в папках на диске) - для этого нужно править код.**  
***Но если ссылка станет недоступной, то бот упадёт в ошибку.***

---

### Наименование файлов (обязательно прописать формат)

Варианты:

1) /audio_dir/audio_1.mp3  
   audio_1 = "audio_1.mp3"
2) /audio_dir/мой_аудио_файл.mp3  
   Тогда
   audio_1 = "мой_аудио_файл.mp3"
___
Начало работы бота: команда `/start`  
___

## Структура логики бота

<img src="./info_other/diagram_bot.png" alt="drawing" width="300"/>