from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.reply import register


router=Router()

@router.message(CommandStart())
async def start_handler(msg:Message):
    await msg.answer("Assalomu Alaykum botga axush kelibsz!",reply_markup=register())