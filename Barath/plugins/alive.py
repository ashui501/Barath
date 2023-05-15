import time 
import random 
import asyncio
from config import HANDLER, OWNER_ID, BARATH
from pyrogram import filters, __version__ as pyrover
from Barath import barath, get_readable_time, StartTime


s1 = """


╔══╗────────╔╗╔╗
║╔╗║───────╔╝╚╣║
║╚╝╚╦══╦═╦═╩╗╔╣╚═╗
║╔═╗║╔╗║╔╣╔╗║║║╔╗║
║╚═╝║╔╗║║║╔╗║╚╣║║║
╚═══╩╝╚╩╝╚╝╚╩═╩╝╚╝
"""


@barath.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
async def alive(_, message):
    name = (await barath.get_me()).first_name
    await message.edit(s1)
    await asyncio.sleep(3)
    await message.delete()
    alive = await message.reply_animation(BARATH, caption="")
    await alive.edit_caption(f"Hello Master **{name}**,\nYou Are Using Barath And Your Current Pyrogram Version Is {pyrover}!")


@barath.on_message(filters.command("ping",prefixes=HANDLER) & filters.user(OWNER_ID))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 3)
     uptime = get_readable_time((time.time() - StartTime))
     await message.edit(f"👾 **System Uptime & Ping**\n=> 🔔 **Ping**: {ping_time}\n=> ⬆️ **Uptime**: {uptime}")
