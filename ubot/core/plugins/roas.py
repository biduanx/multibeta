"""
Amang Kontol
"""
import asyncio
import random
from random import choice
from ubot import *



roast = [
    "**DAR DER DOR, GC AMPAS KU GEDOR**",
]

norak = [
    "**MAEN BOT MULU ALAY, BARU MAKE BOT YA PANTES NORAK!!!**",
    ]

async def roasting_jing(client, message):
    dia = await extract_user(message)
    if dia in DEVS:
        return await message.reply("Lah si anying mo ilang akun lu ?")
    elif dia in await get_seles():
        return await message.reply("Bot lu mo ilang ?")
    else:
        await message.reply(random.choice(roast))
        
async def norak_jing(client, message):
    dia = await extract_user(message)
    if dia in DEVS:
        return await message.reply("Lah si anying mo ilang akun lu ?")
    elif dia in await get_seles():
        return await message.reply("Bot lu mo ilang ?")
    else:
        await message.reply(random.choice(norak))        
        

