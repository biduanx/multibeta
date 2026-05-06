from ubot import *

__MODULE__ = "Prefix"
__HELP__ = <blockquote>"""
Bantuan Untuk Prefix

• Perintah : {0}prefix [trigger]
• Penjelasan : Untuk mengatur handler userbot anda.
"""</blockquote>


@PY.UBOT("prefix")
async def _(client, message):

    await kok_anjeng(client, message)
