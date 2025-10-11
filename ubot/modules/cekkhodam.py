from ubot import *

__MODULE__ = "Cekmek"
__HELP__ = """**BANTUAN UNTUK MODULE CEK**

• Perintah: <code>{0}cekkhodam</code>
• Penjelasan : Untuk melihat khodam nama orang.

• Perintah: <code>{0}cekagama</code>
• Penjelasan : Untuk melihat agama orang.

• Perintah : <code>{0}cekcantik</code>
• Penjelasan : Untuk melihat cantik orang.

• Perintah : <code>{0}cekganteng</code>
• Penjelasan : Untuk melihat ganteng orang.

• Perintah : <code>{0}ceksange</code>
• Penjelasan : Untuk melihat sange orang.

• Perintah : <code>{0}cekkontol</code>
• Penjelasan : Untuk melihat kontol orang.

• Perintah : <code>{0}cekmemek</code>
• Penjelasan : Untuk melihat memek orang.
</blockquote>
"""


@PY.UBOT("cekkhodam")
async def _(client, message):
    await cekkhodam(client, message)
    
@PY.UBOT("cekagama")
async def _(client, message):
    await cekagama(client, message)

@PY.UBOT("cekcantik")
async def _(client, message):
    await cekcantik(client, message)
    
@PY.UBOT("cekganteng")
async def _(client, message):
    await cekganteng(client, message)
    
@PY.UBOT("ceksange")
async def _(client, message):
    await ceksange(client, message)          
    
@PY.UBOT("cekkontol")
async def _(client, message):
    await cekkontol(client, message)
    
@PY.UBOT("cekmemek")
async def _(client, message):
    await cekmemek(client, message)                                                                                
