import telegram
import configx



async def send_telegram_message(u_id, text_send, t_id = configx.tg_api):
    try:
        bot = telegram.Bot(token= t_id)
        await bot.sendMessage(int(u_id), text_send)
    except Exception as e:
        print(e)



send_telegram_message(configx.id_Constantin,"testare 1 SDA")
