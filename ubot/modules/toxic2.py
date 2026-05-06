"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "Toxic2"
__HELP__ = """
<blockquote> Bantuan Untuk Toxic2

• Perintah: <code>{0}per</code>
• Penjelasan: coba aja sendiri.

• Perintah: <code>{0}kendu</code>
• Penjelasan: coba aja sendiri.

• Perintah: <code>{0}badut</code>
• Penjelasan: coba aja sendiri.

• Perintah: <code>{0}zp</code>
• Penjelasan: coba aja sendiri.

• Perintah: <code>{0}pirtual</code>
• Penjelasan: coba aja sendiri.

• Perintah: <code>{0}pea</code>
• Penjelasan: coba aja sendiri.
</blockquote>
"""



@PY.UBOT("per")
async def _(client, message):
    await per(client, message)

@PY.UBOT("kendu")
async def _(client, message):
    await kendu(client, message)
    
@PY.UBOT("badut")
async def _(client, message):
    await badut(client, message)

@PY.UBOT("zp")
async def _(client, message):
    await zp(client, message)

@PY.UBOT("pirtual")
async def _(client, message):
    await pirtual(client, message)

@PY.UBOT("pea")
async def _(client, message):
    await pea(client, message)
