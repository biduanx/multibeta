from ubot import *

__MODULE__ = "ArtiNama"
__HELP__ = """
<blockquote>
• Perintah : <code>{0}artinama</code>
• Penjelasan : Untuk melihat arti nama.
</blockquote>
"""


@PY.UBOT("artinama")
async def _(client, message):
    await artinama(client, message)
    
