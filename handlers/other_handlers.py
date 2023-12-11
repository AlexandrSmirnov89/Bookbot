from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def process_other_message(message: Message):
    await message.answer(f'Я не понимаю команду {message.text}. Для списка доступных команд отправьте /help')
