from telethon.sync import TelegramClient
from telethon import functions
from datetime import datetime
import asyncio
import pytz
import jdatetime
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

tehran_tz = pytz.timezone('Asia/Tehran')

async def update_bio():
    async with TelegramClient("session", api_id, api_hash) as client:
        while True:
            try:
                now = datetime.now(tehran_tz)
                persian_date = jdatetime.date.fromgregorian(date=now.date())
                formatted_date = persian_date.strftime("%Y/%m/%d")
                formatted_time = now.strftime("%H:%M")
                new_bio = f"آخرین بروزرسانی: {formatted_date} - ساعت: {formatted_time}"
                await client(functions.account.UpdateProfileRequest(about=new_bio))
                print(f"بیو آپدیت شد: {new_bio}")
            except Exception as e:
                print(f"خطا: {e}")
            await asyncio.sleep(300)
asyncio.run(update_bio())
