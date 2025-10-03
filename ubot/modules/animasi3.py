"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "Animasi3"
__HELP__ = """
 Bantuan Untuk Animasi3

• Perintah: <code>{0}per</code>
• Penjelasan: coba aja sendiri.

• Perintah: <code>{0}kendu</code>
• Penjelasan: coba aja sendiri.

• Perintah: <code>{0}cinta</code>
• Penjelasan: coba aja sendiri.
"""



@PY.UBOT("per")
async def _(client, message):
    await per(client, message)

@PY.UBOT("kendu")
async def _(client, message):
    await kendu(client, message)
    
@PY.UBOT("cinta")
async def _(client, message):
    await cinta(client, message)    
    
