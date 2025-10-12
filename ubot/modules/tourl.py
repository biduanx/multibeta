from ubot import *

__MODULE__ = "ToUrl"
__HELP__ = """
<blockquote><b>Bantuan untuk tourl

perintah : <code>{0}tourl</code> [reply media/text]
    mengapload media/text ke catbox.moe</b></blockquote>
"""

@PY.UBOT("tourl")
async def _(client, message):
    await tourl(client, message)
    
