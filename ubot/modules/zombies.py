from ubot import *

__MODULE__ = "Zombies"
__HELP__ = """
<blockquote> Bantuan Untuk Zombies

• Perintah: <code>{0}zombies</code>
• Penjelasan: Untuk mengeluarkan akun depresi digrup anda.
</blockquote>
"""

@PY.UBOT("zombies")
async def _(client, message):
    await zombies_cmd(client, message)
