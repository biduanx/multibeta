from ubot import *

__MODULE__ = "Convert"
__HELP__ = """
 Bantuan Untuk Convert
 
• Perintah : <code>{0}toimg</code> [balas stiker/gif]
• Penjelasan : Merubah stiker/gif ke foto.

• Perintah : <code>{0}tosticker</code> [balas ke foto]
• Penjelasan : Merubah foto ke stiker.

• Perintah : <code>{0}togif</code> [balas stiker]
• Penjelasan : Merubah stiker ke gif.

• Perintah : <code>{0}toaudio</code> [balas video]
• Penjelasan : Merubah video menjadi audio mp3.

• Perintah : <code>{0}curi</code> [balas pesan]
• Penjelasan : Untuk mencuri media timer, cek pesan tersimpan
"""


@PY.UBOT("toimg")
async def _(client, message):
    await convert_photo(client, message)


@PY.UBOT("tosticker")
async def _(client, message):
    await convert_sticker(client, message)


@PY.UBOT("togif")
async def _(client, message):
    await convert_gif(client, message)


@PY.UBOT("toaudio")
async def _(client, message):
    await convert_audio(client, message)


@PY.UBOT("curi")
async def _(client, message):
    await colong_cmn(client, message)
