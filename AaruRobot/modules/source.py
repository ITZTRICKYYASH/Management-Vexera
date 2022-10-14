from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from AaruRobot import pbot as client


Aaru = "https://telegra.ph/file/6ccab5bc360325388e2c4.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Aaru,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ᴀᴀʀᴜ ✘ ʀᴏʙᴏᴛ-🇮🇳](https://t.me/DollxSpam_BOT)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [⏤‌❥‌ 🖤𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ¤‌๋‌ࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧ𖣔ꠋꠋ𑲭𑲭𑲭🦋⃟≛⃝🖤҉𓆩⍣⃟N1x乛DÕLL𓆪‌⍣⃟❤︎𓆪‌⍣⃟𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭](https://t.me/DollxSpam_BOT)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴀᴀʀᴜ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴅᴇᴠᴇʟᴏᴘᴇʀ •", url="https://t.me/DollxSpam_BOT"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://t.me/DollxSpam_BOT")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
