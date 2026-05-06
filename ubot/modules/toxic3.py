"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "Toxic3"
__HELP__ = """
<blockquote> Bantuan Untuk Toxic3

• Perintah: <code>{0}aliansi</code>
• Penjelasan: coba sendiri mek.

• Perintah: <code>{0}jablay</code>
• Penjelasan: coba sendiri mek.

• Perintah: <code>{0}ganteng</code>
• Penjelasan: coba sendiri mek.

• Perintah: <code>{0}gcs</code>
• Penjelasan: coba sendiri mek.

• Perintah: <code>{0}alay</code>
• Penjelasan: coba sendiri mek.

• Perintah: <code>{0}bertitle</code>
• Penjelasan: coba sendiri mek.

• Perintah: <code>{0}war</code>
• Penjelasan: coba sendiri mek.
</blockquote>
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
    
@PY.UBOT("gcs")
async def _(client, message):
    await gcs(client, message)

@PY.UBOT("alay")
async def _(client, message):
    await alay(client, message)
    
@PY.UBOT("bertitle")
async def _(client, message):
    await bertitle(client, message)    

@PY.UBOT("war")
async def _(client, message):
    await war(client, message)    
