from pyrogram import filters

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import add_off, add_on
from AnonXMusic.utils.decorators.language import language

from strings.filters import command

@app.on_message(command(["تفعيل السجلات"]) & SUDOERS)
@language
async def enable_notifications(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    
    await add_on(2)
    await message.reply_text(_["log_2"])

@app.on_message(command(["تعطيل السجلات"]) & SUDOERS)
@language
async def disable_notifications(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    
    await add_off(2)
    await message.reply_text(_["log_3"])
