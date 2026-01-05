from ubot import *


__MODULE__ = "Vc"
__HELP__ = """
<blockquote> Bantuan Untuk Voice Chat

• Perintah: <code>{0}startvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}stopvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.

• Perintah: <code>{0}jvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}lvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.
</blockquote>
"""




@PY.UBOT("startvc")
async def _(client, message):
    await start_vctools(client, message)


@PY.UBOT("stopvc")
async def _(client, message):
    await stop_vctools(client, message)


@PY.UBOT("jvc", FILTERS.ME_USER)
async def _(client, message):
    await join_os(client, message)


@PY.UBOT("lvc", FILTERS.ME_USER)
async def _(client, message):
    await turun_os(client, message)





