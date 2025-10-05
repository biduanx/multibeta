"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "Toxic"
__HELP__ = """
 Bantuan Untuk Toxic

• Perintah: <code>{0}roas</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.
"""



@PY.UBOT("roas")
async def _(client, message):
    await roasting_jing(client, message)
