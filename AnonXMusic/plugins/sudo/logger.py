from pyrogram import filters
from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import add_off, add_on
from AnonXMusic.utils.decorators.language import language
from strings.filters import command

@app.on_message(command(["تفعيل الاشعارات"]) & SUDOERS)
@language
async def enable_notifications(client, message, _):  
    await add_on(2)
    await message.reply_text("تم تفعيل الإشعارات بنجاح!")

@app.on_message(command(["تعطيل الاشعارات"]) & SUDOERS)
@language
async def disable_notifications(client, message, _):  
    await add_off(2)
    await message.reply_text("تم تعطيل الإشعارات بنجاح!")
