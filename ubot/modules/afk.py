from ubot import *

__MODULE__ = "afk"
__HELP__ = """
<b>『 Bantuan Untuk Afk 』</b>

  <b>• Perintah:</b> <code>{0}afk</code></code>
  <b>• Penjelasan:</b> untuk mengaktifkan afk 

  <b>• Perintah:</b> <code>{0}unafk</code></code>
  <b>• Penjelasan:</b> untuk menonaktifkan afk
"""

@PY.UBOT("afk")
async def _(client, message):
    reason = get_arg(message)
    afk_handler = AwayFromKeyboard(client, message, reason)
    await afk_handler.set_afk()


@PY.AFK(True)
async def _(client, message):
    afk_handler = AwayFromKeyboard(client, message)
    await afk_handler.get_afk()


@PY.UBOT("unafk")
async def _(client, message):
    afk_handler = AwayFromKeyboard(client, message)
    return await afk_handler.unset_afk()