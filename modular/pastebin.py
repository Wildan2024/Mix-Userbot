################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 @ CREDIT : NAN-DEV
"""
################################################################

import re
from gc import get_objects

import aiofiles
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")

__modles__ = "Pastebin"
__help__ = """
 Help Command Pastebin

• Perintah : <code>{0}paste</code> [balas pesan]
• Penjelasan : Untuk mengupload teks ke pastebin.
"""


@ky.inline("^paste_an")
async def _(c, iq):
    teks = "Done Pastebin."
    try:
        _id = int(iq.query.split()[1])
        m = [obj for obj in get_objects() if id(obj) == _id][0]
        ez = await user.get_messages(m.chat.id, m.reply_to_message_id)
        with open("ez.txt", "w") as file:
            file.write(ez.text)
        async with aiofiles.open("ez.txt", mode="r") as f:
            content = await f.read()
        link = await paste(content)
        kb = InlineKeyboardMarkup([[InlineKeyboardButton(text="Paste Link", url=link)]])
        hasil = [
            InlineQueryResultPhoto(
                photo_url=link, title="kon", reply_markup=kb, caption=teks
            )
        ]
        await c.answer_inline_query(
            iq.id,
            cache_time=0,
            results=hasil,
        )
    except Exception as e:
        LOGGER.warning(f"Error: {e}")


@ky.ubot("paste", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    if not m.reply_to_message:
        return await m.reply_text(f"{em.gagal} Silahkan balas ke pesan.")
    try:
        x = await c.get_inline_bot_results(bot.me.username, f"paste_an {id(m)}")
        return await c.send_inline_bot_result(m.chat.id, x.query_id, x.results[0].id)
    except Exception as e:
        return await m.reply(e)
