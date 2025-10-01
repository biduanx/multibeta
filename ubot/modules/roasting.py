"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "Roasting"
__HELP__ = """
 Bantuan Untuk Roasting

• Perintah: <code>{0}roast</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}norak</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.
"""



@PY.UBOT("roast")
async def _(client, message):
    await roasting_jing(client, message)
    
@PY.UBOT("norak")
async def _(client, message):
    await roasting_jing(client, message)    

