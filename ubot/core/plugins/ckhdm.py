import asyncio
import random

from ubot import *

async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴀɴᴊᴇɴɢ🤓")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ʜᴀsɪʟ ᴄᴇᴋ ᴋʜᴏᴅᴀᴍ:</b>
 <blockquote>
 •ɴᴀᴍᴀ : {nama}
 •ᴋʜᴏᴅᴀᴍɴʏᴀ : {pick_random(['lonte gurun', 'dugong', 'macan yatim', 'buaya darat', 'kanjut terbang', 'kuda kayang', 'janda salto', 'lonte alas', 'jembut singa', 'gajah terbang', 'kuda cacat', 'jembut pink', 'sabun bolong'])}
 •ɴɢᴇʀɪ ʙᴇᴛ ᴊɪʀ ᴋʜᴏᴅᴀᴍɴʏᴀ
  **ɴᴇxᴛ ᴄᴇᴋ ᴋʜᴏᴅᴀᴍɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ.**</blockquote>       
      """
        await message.edit(hasil)
    except BaseException:
        pass

KHODAM_LIST = [
    "1% (JELEK BINGIT)🤮", "55% (MAYAN)🙂", "30% (DEMPUL)🙃", "70% (CANTIK TAPI AGAK IRENG)😉",
    "90% (CANTIKNYA PAS)😎", "100% (CANTIK+TOBRUT)🤯", "4% (IRENG)🤢", "10% (IRENG+TEPOS)😖", "1000% (CANTIK+TOBRUT+MANIS)😱"
]


async def cekcantik(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("⚠️ Gunakan format: cekkctkn [nama]")

    nama = args[1]
    khodam = random.choice(KHODAM_LIST)
    hasil = f"<blockquote><b>🤭HASIL KECANTIKAN🤭\n\n=👩 Nama: `{nama}`\n Persen: `{khodam}`</blockquote></b>"
    await message.reply_text(hasil)

AGAMA_LIST = [
    "HINDU","ATEIS (GAK PUNYA AGAMA","ISLAM","KRISTEN","BUDHA","KATOLIK","KRISTEN PROTESTAN","ISLAM KTP","KONGHUCU",
]


async def cekagama(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.reply_text("<blockquote><b>⚠️ Gunakan format: .cekagama [nama]</blockquote></b>")

    nama = args[1]
    agama = random.choice(AGAMA_LIST)
    hasil = f'''<blockquote><b>
    HASIL DETEKSI AGAMA DARI {nama}
    ╭───────────────────────
    ├ ɴᴀᴍᴀ : `{nama}`
    ├ ᴀɢᴀᴍᴀ: `{agama}`
    ├ sᴇʟᴀᴍᴀᴛ ʏᴀ ᴀɢᴀᴍᴀ ɴʏᴀ ᴄᴏᴄᴏᴋ ᴋᴏᴋ
    ╰────────────────────────
    ɴᴏᴛᴇ ᴍᴀᴀғ ʏᴀ {nama} ᴄᴜᴍᴀ ʙᴇᴄᴀɴᴅᴀ ᴋᴏᴋ 😁
    
    </blockquote></b>'''
    await message.reply_text(hasil)

async def cekkontol(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴀɴᴊᴇɴɢ🤓")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ ᴋᴏɴᴛᴏʟ {nama} </b>
<blockquote><b>╭───「 ʜᴀsɪʟ ᴄᴇᴋ ᴋᴏɴᴛᴏʟ 」───</b>
<b>┆• ᴡᴀʀɴᴀ ᴋᴏɴᴛᴏʟ : {pick_random(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆• ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {pick_random(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆• ᴜᴋᴜʀᴀɴ ᴋᴏɴᴛᴏʟ : {pick_random(['16 cm', '10 cm', '15 cm', '6 cm', '1 cm', '3 cm'])}</b>
<b>┆• ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {pick_random(['bengkok', 'bengkok dikit', 'lurus', 'panjang kecil', 'lebar', 'tumpul'])}</b>
<b>╰──────────────────────</b></blockquote>
  <b>ɴᴇxᴛ ᴄᴇᴋ ᴋᴏɴᴛᴏʟɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ.</b>   
      """
        await message.edit(hasil)
    except BaseException:
        pass

async def cekmemek(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴀɴᴊᴇɴɢ🤓")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ ᴍᴇᴍᴇᴋ {nama} </b>
<blockquote><b>╭───「 ʜᴀsɪʟ ᴄᴇᴋ ᴍᴇᴍᴇᴋ 」───</b>
<b>┆• ᴡᴀʀɴᴀ ᴍᴇᴍᴇᴋ : {pick_random(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆• ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {pick_random(['irenk', 'pink', 'rainbow', 'itam cok', 'kuning'])}</b>
<b>┆• ᴜᴋᴜʀᴀɴ ʟᴏʙᴀɴɢ : {pick_random(['16 inc', '10 inc', '15 inc', '6 inc', '1 inc', '3 inc'])}</b>
<b>┆• ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {pick_random(['berjembut', 'dah jebol', 'bau trasi', 'berlendir', 'lebar itam', 'sempit'])}</b>
<b>╰──────────────────────</b></blockquote>
  <b>ɴᴇxᴛ ᴄᴇᴋ ᴍᴇᴍᴇᴋɴʏᴀ sɪᴀᴘᴀ ʟᴀɢɪ.</b>   
      """
        await message.edit(hasil)
    except BaseException:
        pass

async def ceksange(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴀɴᴊᴇɴɢ🤓")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
<b>𖤐 ᴄᴇᴋ sᴀɴɢᴇ</b>
<blockquote><b>╭───「 ʜᴀsɪʟ ᴄᴇᴋ sᴀɴɢᴇ 」───</b>
<b>┆• ɴᴀᴍᴀ :  {nama} </b>
<b>┆• sᴀɴɢᴇ : {pick_random(['90%', '95%', '75%', '85%', '100%'])}</b>
<b>┆• sᴀɴɢᴇᴀɴ ᴋᴏɴᴛᴏʟ </b>
<b>╰──────────────────────</b></blockquote>
  <b>ɴᴇxᴛ ᴄᴇᴋ sᴀɴɢᴇ sɪᴀᴘᴀ ʟᴀɢɪ.</b>   
      """
        await message.edit(hasil)
    except BaseException:
        papass

async def cekganteng(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
 <b>𖤐 ʜᴀsɪʟ ᴄᴇᴋ ɢᴀɴᴛᴇɴɢ:</b>
╭───────────────────────
├ •ɴᴀᴍᴀ : {nama}
├ •ɢᴀɴᴛᴇɴɢ : {pick_random(['ᴋᴀʏᴀ ᴋᴛʟ', 'ᴅɪᴋɪᴛ', 'ʙᴀɴʏᴀᴋ', 'sᴇᴛᴇɴɢᴀʜ', 'sᴇᴘᴇʀᴀᴘᴀᴛ', 'sᴇ ᴛᴇᴛᴇ'])}
├ •ɴɢᴇʀɪ ʙᴇᴛ ᴊɪʀ
╰────────────────────────
  **ɴᴇxᴛ ᴄᴇᴋ ɢᴀɴᴛᴇɴɢ sɪᴀᴘᴀ ʟᴀɢɪ.**       
      """
        await message.edit(hasil)
    except BaseException:
        pass
