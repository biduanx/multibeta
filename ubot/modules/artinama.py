from ubot import *

__MODULE__ = "Artinama"
__HELP__ = <blockquote>"""
Bantuan Untuk Arti Nama

Perintah:
<code>{0}artinama nama</code> → Mengartikan dengan nama
"""</blockquote></b>


@PY.UBOT("artinama")
async def _(client, message):
    await artinama(client, message)
    
