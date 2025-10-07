"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "Toxic"
__HELP__ = """
 Bantuan Untuk Toxic

• Perintah: <code>{0}pp</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}kn</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}mk</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.
"""



@PY.UBOT("pp")
async def _(client, message):
    await pp_jing(client, message)

@PY.UBOT("kn")
async def _(client, message):
    await kn_jing(client, message)

@PY.UBOT("mk")
async def _(client, message):
    await mk_jing(client, message)
