from ubot import *

__MODULE__ = "ArtiNama"
__HELP__ = """

• Perintah : <code>{0}cekmemek</code>
• Penjelasan : Untuk melihat arti nama.
</blockquote>
"""


@PY.UBOT("artinama")
async def _(client, message):
    await artinama(client, message)
    
