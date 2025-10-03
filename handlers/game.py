from aiogram import Router
from aiogram.types import Message
from utils.crypto import verify_payment_fixed
from utils.logic import check_win, get_multiplier
from config import CHANNEL_ID
import random

router = Router()

@router.message()
async def handle_bet(message: Message):
    if not message.text.lower().startswith("куб "):
        return

    bet = message.text[4:].strip().lower()
    user_id = message.from_user.id

    payment = await verify_payment_fixed(user_id, bet)
    if not payment:
        await message.reply("❌ Оплата не найдена или неверный комментарий.")
        return

    roll = random.randint(1, 6)
    win = check_win(bet, roll)
    multiplier = get_multiplier(bet)
    result_text = f"🎲 Выпало: {roll}\nСтавка: {bet}\n"

    if win:
        payout = round(payment["amount"] * multiplier, 2)
        result_text += f"✅ Победа! Выигрыш: {payout} {payment['currency']}"
    else:
        result_text += "❌ Проигрыш."

    await message.bot.send_message(CHANNEL_ID, result_text)
    await message.reply(result_text)