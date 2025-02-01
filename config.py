import re, os, time
from pyrogram.types import Message
from pyrogram import Client, filters
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 

DEV=[6299192020]

ADMIN =[]

@Client.on_message(filters.command("aadmin") & filters.user(DEV))
async def set_target_channel(client , message):
    
    # Extract channel ID from the message
    if len(message.command) > 1:
        channel_id = message.command[1]
        try:
            admin_id = int(channel_id)
            ADMIN.append(admin_id)
            await message.reply_text("New Admin id {admin_id} added successfully ✅")
       
        except ValueError:   
            await message.reply_text("Invalid channel ID. Please provide a valid channel ID.")
    else:
        await message.reply_text("Please provide a channel ID after the command. Example: /set_target 123456789")

@Client.on_message(filters.command("radmin") & filters.user(DEV))
async def set_target_channel(client , message):
    

    # Extract channel ID from the message
    if len(message.command) > 1:
        channel_id = message.command[1]
        try:
            admin_id = int(channel_id)
            if admin_id in ADMIN:
                ADMIN.remove(admin_id)
                await message.reply_text(" 🗑️Admin id {admin_id} Delete successfully ✅")
            else:
                await Message.reply_text(" There is No Admin in this Id 🫅")
        except ValueError:
            await message.reply_text("Invalid channel ID. Please provide a valid channel ID.")
    else:
        await message.reply_twxt("Please provide a channel ID after the command. Example: /set_target 123456789")


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21740783")
    API_HASH  = os.environ.get("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7435219753:AAFzGs09ktzVU6Zt7NI_ChfVyAAPlDDe9FU") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","boyrokey00")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://boyrokey00:rajan123@cluster0.4fhuu.mongodb.net/")
    PORT = os.environ.get("PORT", "8020")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/29a3acbbab9de5f45a5fe.jpg")
    
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0" ))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.

<b>Bot Is Made By @AshutoshGoswami24</b>

<b><a href='https://github.com/AshutoshGoswami24/Auto-Rename-Bot'>AshutoshGoswami24/Auto-Rename-Bot.git</a></b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ `[episode]` :- To Replace Episode Number
✓ `[quality]` :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @AshutoshGoswami24</code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>🧑‍💻 Developer :</b> <a href='https://t.me/AshutoshGoswami24'>PandaWep</a>
    
<b>♻️ Bot Made By :</b> @AshutoshGoswami24"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @AshutoshGoswami24
╰━━━━━━━━━━━━━━━➣ </b>"""
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>My UPI - PandaWep@ybl</b> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Joine @AshutoshGoswami24 To Help """
