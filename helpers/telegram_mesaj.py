import telegram
import configx
import asyncio



bot = telegram.Bot(token= configx.tg_api)
async def send_telegram_message(u_id, text_send):
    try:
        async with bot:
            await bot.sendMessage(int(u_id), text_send)
    
    except Exception as e:
        print(e)

    