from ubot import *

__MODULE__ = "Quotly"
__HELP__ = <blockquote>"""
Bantuan Untuk Quotly

• Perintah: <code>{0}q</code> [text/reply to text/media]
• Penjelasan: Untuk merubah text menjadi sticker.

• Perintah: <code>{0}q</code> [white/black/red/pink]
• Penjelasan: Untuk merubah latar belakang quote.

• Perintah : <code>{0}kang</code> [balas ke stiker]
• Penjelasan : Untuk membuat kosum stiker pak.
"""</blockquote>


@PY.UBOT("q")
async def _(client, message):
    await quotly_cmd(client, message)

@PY.UBOT("kang")
async def _(client, message):
    await kang(client, message)
