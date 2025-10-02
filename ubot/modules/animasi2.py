"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "animasi2"
__HELP__ = """
 Bantuan Untuk animasi2

• Perintah: <code>{0}aliansi</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}jablay</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}ganteng</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.
"""



@PY.UBOT("aliansi")
async def _(client, message):
    await aliansi(client, message)

@PY.UBOT("jablay")
async def _(client, message):
    await jablay(client, message)
    
@PY.UBOT("ganteng")
async def _(client, message):
    await ganteng(client, message)    
