from ubot import *

__MODULE__ = "ArtiNama"
__HELP__ = """
<blockquote><b>Bantuan Untuk Arti Nama</b>

Perintah:
<code>{0}artinama [nama]</code> → Mengartikan dengan nama</blockquote></b>
"""


@PY.UBOT("artinama")
async def _(client, message):
    await artinama(client, message)
    
