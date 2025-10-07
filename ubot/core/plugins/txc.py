"""
Amang Kontol
"""
import asyncio
import random
from random import choice
from ubot import *


pp = [
    "**PP LU KEMANA DAH? LAGI DEPRESI? APA GIMANA ? AWOAKWOAK 😆**",
]

kn = [
    "**KONTOL MASIH ITEM AJA SO SO AN NGAJAK VCS ANJING ?**",
]

mk = [
    "**SOSOAN OPEN VCS MEMEK LU INTEM ANJENGGG BAU TERASI IDIHHHH!!**",
]



async def pp_jing(client, message):
    dia = await extract_user(message)
    if dia in DEVS:
        return await message.reply("Lah si anying mo ilang akun lu ?")
    elif dia in await get_seles():
        return await message.reply("Bot lu mo ilang ?")
    else:
        await message.reply(random.choice(pp))
        
async def kn_jing(client, message):
    dia = await extract_user(message)
    if dia in DEVS:
        return await message.reply("Lah si anying mo ilang akun lu ?")
    elif dia in await get_seles():
        return await message.reply("Bot lu mo ilang ?")
    else:
        await message.reply(random.choice(kn))
        
async def mk_jing(client, message):
    dia = await extract_user(message)
    if dia in DEVS:
        return await message.reply("Lah si anying mo ilang akun lu ?")
    elif dia in await get_seles():
        return await message.reply("Bot lu mo ilang ?")
    else:
        await message.reply(random.choice(mk))                        
