from ubot import *

__MODULE__ = "Sangmata"
__HELP__ = """
<blockquote> Bantuan Untuk Sangmata

• Perintah: <code>{cobadah}sg</code> [user_id/reply user]
• Penjelasan: Untuk memeriksa histori nama/username.
</blockquote>
"""


@PY.UBOT("sg")
async def _(client, message):
    await sg_cmd(client, message)
