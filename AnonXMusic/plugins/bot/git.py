from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AnonXMusic import app
from config import CHANNEL_SUDO

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not CHANNEL_SUDO:
        return
    try:
        try:
            await app.get_chat_member(CHANNEL_SUDO, msg.from_user.id)
        except UserNotParticipant:
            if CHANNEL_SUDO.isalpha():
                link = "https://t.me/" + CHANNEL_SUDO
            else:
                chat_info = await app.get_chat(CHANNEL_SUDO)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"~︙عذراً عزيزي {msg.from_user.mention} \n~︙عليك الأشتراك في قناة البوت \n~︙قناة البوت : @{CHANNEL_SUDO} .",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("⦗ قناة الاشتراك ⦘", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat {Muntazer}!")
