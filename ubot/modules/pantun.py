from ubot import *

__MODULE__ = "pantun"
__HELP__ = """
 Bantuan Untuk pantun

• Perintah: <code>{0}sepat</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}ngangkang</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}hancur</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}kenalan</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}soms</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}sirik</code>
• Penjelasan: Coba sendiri.

• Perintah: <code>{0}imut</code>
• Penjelasan: Coba sendiri.

"""


@PY.UBOT("sepat")
async def _(client, message):
    await sepat(client, message)

@PY.UBOT("ngangkang")
async def _(client, message):
    await ngangkang(client, message)


@PY.UBOT("hancur")
async def _(client, message):
    await hancur(client, message)


@PY.UBOT("kenalan")
async def _(client, message):
    await kenalan(client, message)

@PY.UBOT("soms")
async def _(client, message):
    await soms(client, message)

@PY.UBOT("sirik")
async def _(client, message):
    await sirik(client, message)

@PY.UBOT("imut")
async def _(client, message):
    await dornembak(client, message)

