from ubot import *


__MODULE__ = "VoiceChat"
__HELP__ = """
Bantuan Untuk Voice Chat

• Perintah: <code>{0}startvc</code>
• Penjelasan: Untuk memulai voice chat grup.

• Perintah: <code>{0}joinvcs</code>
• Penjelasan: Untuk bergabung voice chat grup

• Perintah: <code>{0}leavevcs</code>
• Penjelasan: Untuk keluar voice chat grup

• Perintah: <code>{0}stopvc</code>
• Penjelasan: Untuk mengakhiri voice chat grup.
"""



@PY.UBOT("startvc")
async def _(client, message):
    await start_vctools(client, message)


@PY.UBOT("stopvc")
async def _(client, message):
    await stop_vctools(client, message)


@PY.UBOT("joinvcs", FILTERS.ME_USER)
async def _(client, message):
    await join_os(client, message)


@PY.UBOT("leavevcs", FILTERS.ME_USER)
async def _(client, message):
    await turun_os(client, message)


