# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>📝 Tentang Bot ini 📝\n\n 🎗 ᴏᴡɴᴇʀ ʙᴏᴛ : <a href='https://t.me/SkandalID'>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>\n\n 🗂 ᴍᴀɴᴀɢᴇ ʙʏ : <a href='https://t.me/GreyStore'>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>\n\n 💌 ᴏᴡɴᴇʀ ʀᴇᴘᴏ : <a href='https://t.me/GreyInHere'>ᴋʟɪᴋ ᴅɪsɪɴɪ</a>\n\n        <a href='https://t.me/GreyStore'>ᴊᴀsᴀ ʙɪᴋɪɴ ʙᴏᴛ ᴍᴜʀᴀʜ</a>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
