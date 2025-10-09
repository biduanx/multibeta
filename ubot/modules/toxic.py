"""
Amwang Kontol
"""

from ubot import *

__MODULE__ = "Toxic"
__HELP__ = """
<blockquote> Bantuan Untuk Toxic

• Perintah: <code>{0}title</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}wah</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}ewe</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}texas</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}item</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.

• Perintah: <code>{0}memeg</code>
• Penjelasan: Untuk caci maki manusia gak tau diri.
</blockquote>
"""


@PY.UBOT("title")
async def _(client, message):
    await title(client, message)
    
@PY.UBOT("wah")
async def _(client, message):
    await wah(client, message)    
    
@PY.UBOT("ewe")
async def _(client, message):
    await ewe(client, message)    
    
@PY.UBOT("texas")
async def _(client, message):
    await texas(client, message)    
    
@PY.UBOT("item")
async def _(client, message):
    await item(client, message)   
    
@PY.UBOT("memeg")
async def _(client, message):
    await memeg(client, message)               

