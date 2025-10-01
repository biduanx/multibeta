################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || @iamuputt
"""
################################################################


import asyncio

from pyrogram import *

from ubot import *

async def sepat(client, message):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Ikan sepat ikan tongkol**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**CAKEEEEPPPPP**")
    await asyncio.sleep(2)
    await putt.edit("**Mukaa lu kek kontolll.**😆")


async def ngangkang(client, message):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Beli batik di tanah abang..**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**Kamu cantikkk, Tapi sayang...**")
    await asyncio.sleep(2)
    await putt.edit("**Hobby nya ngangkang** 😆🤪")


async def hancur(client, message):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Makan semur, Masih anget..**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**CAKEEEEPPPPP**")
    await asyncio.sleep(2)
    await putt.edit("**Muka kamu hancur, Kok pakai banget.🤪**")


async def kenalan(client, message):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Barang antik, ditarik andong**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**CAKEEEEPPPPP**")
    await asyncio.sleep(2)
    await putt.edit("**Haii cantikk, kenalan donggg. 😋**")


async def soms(client, message):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Makan sambel ulek pakai kedondong**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**CAKEEEEPPPPP**")
    await asyncio.sleep(2)
    await putt.edit("**Gapapa jelekk yang penting sombong. 😋**")


async def sirik(client, message):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply(
        "**Rambut panjang di sisirin**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(2)
    await putt.edit("**Sambil seduh dua extra joss**")
    await asyncio.sleep(2)
    await putt.edit("**Cerita dikit di nyinyirin**")
    await asyncio.sleep(2)
    await putt.edit("**Kalo sirikk bilang bosss..**🖕")


async def imut(client, message):
    if m.reply_to_message and m.reply_to_message.from_user.id in DEVS:
        await m.reply("**AKUN LO MO ILANG BANGSAT??**")
        return
    putt = await m.reply("**Wajahmu memang imut**", reply_to_message_id=ReplyCheck(m))
    await asyncio.sleep(2)
    await putt.edit("**Bodimu kaya siput**")
    await asyncio.sleep(2)
    await putt.edit("**Tingkahmu membuatku salutt**")
    await asyncio.sleep(2)
    await putt.edit("**Tapi sayang hobimu kentutt.** 😭🤌")
    
    
