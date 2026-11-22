# В твоем коде логгера (записи логов в консоль) пока нет, но раз на скриншоте эта папка есть, я дам тебе заготовку. Ты можешь пока не использовать этот файл, но когда захочешь выводить красивые логи в консоль с датой и временем — он пригодится.

# utils/logger.py — Модуль для настройки логирования (записи событий).


import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)