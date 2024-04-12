import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message


from X.helpers.PyroHelpers import GetChatID, ReplyCheck
from .help import * 

@Client.on_message(filters.command(["genshin"], ".") & filters.me)
async def give_genshin(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/genshin"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
              )