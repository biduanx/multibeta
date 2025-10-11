from ubot import *

__MODULE__ = "ᴄᴇᴋᴋʜᴏᴅᴀᴍ"
__HELP__ = """**「 BANTUAN UNTUK MODULE CEK KHODAM 」**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .cekkhodam**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴋʜᴏᴅᴀᴍ ɴᴀᴍᴀ ᴏʀᴀɴɢ**"""


@PY.UBOT("cekkhodam")
async def _(client, message):
    await cekkhodam(client, message)
