from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from AloneXMusic import app
from AloneXMusic.core.call import Alone
from AloneXMusic.utils import bot_sys_stats
from AloneXMusic.utils.decorators.language import language
from AloneXMusic.utils.inline.play import close_keyboard

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=random.choice(PING_IMG_URL),
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Alone.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
