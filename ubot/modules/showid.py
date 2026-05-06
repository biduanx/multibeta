from ubot import *


__MODULE__ = "ShowID"
__HELP__ = """
<blockquote> Bantuan Untuk Show ID

• Perintah: <code>{0}id</code>
• Penjelasan: Untuk mengetahui ID dari user/grup/channel.
</blockquote>
"""


@PY.UBOT("id")
async def _(client, message):
    await id_cmd(client, message)
