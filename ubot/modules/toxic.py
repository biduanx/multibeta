"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "toxic"
__HELP__ = """
 Bantuan Untuk toxic

• Perintah: <code>{0}petinggi</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}aliansi</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.
"""



@PY.UBOT("petinggi")
async def _(client, message):
    await petinggi(client, message)
    
@PY.UBOT("aliansi")
async def _(client, message):
    await aliansi(client, message)

