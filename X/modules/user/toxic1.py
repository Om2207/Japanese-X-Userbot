# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

#REMAKE BY NOBITA XD AND TRYTOLIVEALONE




import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply
from X.utils import extract_user

from .help import *


@Client.on_message(filters.command("toxicity", CMD_HANDLER) & filters.me)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**This command is forbidden to be used by my developers**"
        )
    xx = await edit_or_reply(message, "**WOW**")
    await asyncio.sleep(1.5)
    await xx.edit("**THE DICK OF AN ILLEGAL CHILD**")
    await asyncio.sleep(1.5)
    await xx.edit("**THE ONES BORN VILE AND UGLY**")
    await asyncio.sleep(1.5)
    await xx.edit("**WHAT ARE YOU DOING HERE DICK**")
    await asyncio.sleep(1.5)
    await xx.edit("**HERE I DON'T ACCEPT DESPITE PEOPLE LIKE YOU**")
    await asyncio.sleep(1.5)
    await xx.edit("**JUST PULL IT OUT THERE YOU PEPEK**")
    await asyncio.sleep(1.5)
    await xx.edit("**THERE'S NO POINT FOR YOU HERE YOU BITCH**")
    await asyncio.sleep(1.5)
    await xx.edit("**BYE DESPITE HUMAN WHO WAS BORN IN A POOR AND BAD FAMILY**")
    await asyncio.sleep(1.5)

@Client.on_message(filters.command("idiot", CMD_HANDLER) & filters.me)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**This command is forbidden to be used by my developers**"
        )
    xx = await edit_or_reply(message, "**WOOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**WOW IDIOOTT**")
    await asyncio.sleep(1.5)
    await xx.edit("**YOU ARE AN IDIOT**")
    await asyncio.sleep(1.5)
    await xx.edit("**WHAT ARE YOU DOING HERE DICK**")
    await asyncio.sleep(1.5)
    await xx.edit("**HERE YOU DON'T ACCEPT RICH IDIOT PEOPLE WHO FUCK YOU**")
    await asyncio.sleep(1.5)
    await xx.edit("**JUST PULL IT OUT THERE, YOU SLUT**")
    await asyncio.sleep(1.5)
    await xx.edit("**THERE'S NO POINT FOR YOU HERE YOU BITCH**")
    await asyncio.sleep(1.5)
    await xx.edit("**THE DRUGS OF THE STUPID IDIOT CHILD IS UNIVERSAL**")
    await asyncio.sleep(1.5)


add_command_help(
    "•─╼⃝𖠁 ᴛᴏxᴄɪ𝟷",
    [
        ["toxicity", "Tᴏ ɪᴜᴅɢᴇ ɪʟʟᴇɢɪᴛɪᴍᴀᴛᴇ ᴄʜɪʟᴅʀᴇɴ ʟɪᴋᴇ ʏᴏᴜ"],
        ["idiot", "Tᴏ Cᴏɴᴛᴀɪɴ ᴀɴ Iᴅɪᴏᴛ Kɪᴅ Lɪᴋᴇ ᴜ"],
    ]
  ) 
