from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """
✪ 𝐖εℓ¢σмє 𝐅σя 𝐀𝐫ɴᴀᴠ 𝐑єρσѕ ✪
 
 ➲ ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ ᴋʏᴀ ᴍᴇʀᴇ @link_copied ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ᴍᴀᴋʜᴀɴ ᴊᴇꜱᴇ ᴄʜᴀʟᴇɢᴀ ✰
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/enjoy_your_life143"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/cute_arnavsingh"),
          ],
               [
                InlineKeyboardButton("𝗔𝗕𝗢𝗨𝗧 𝗔𝗥𝗡𝗔𝗩", url=f"https://t.me/aboutarnav"),

],
[
InlineKeyboardButton("𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗚𝗥𝗢𝗨𝗣", url=f"https://t.me/enjoy_your_life143"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/2ce1561ccac8b80b65691.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
