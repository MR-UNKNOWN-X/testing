# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/MR-UNKNOWN-X/testing/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/MR-UNKNOWN-X/testing/blob/main/LICENSE/>.

"""
✘ Commands Available -

•`{i}schedule <text/reply to msg> <time>`
    In time u can use second as number, or like 1h or 1m
    eg. `{i}schedule Hello 100` It deliver msg after 100 sec.
    eg. `{i}schedule Hello 1h` It deliver msg after an hour.
"""

from datetime import timedelta

from . import *


@ultroid_cmd(pattern="schedule ?(.*)")
async def _(e):
    x = e.pattern_match.group(1)
    xx = await e.get_reply_message()
    if x and not xx:
        y = x.split(" ")[-1]
        k = x.replace(y, "")
        if y.isdigit():
            await ultroid_bot.send_message(
                e.chat_id, k, schedule=timedelta(seconds=int(y))
            )
            await eod(e, "`Scheduled msg Succesfully`")
        else:
            try:
                z = await ban_time(e, y)
                await ultroid_bot.send_message(e.chat_id, k, schedule=z)
                await eod(e, "`Scheduled msg Succesfully`")
            except BaseException:
                await eod(e, "`Incorrect Format`")
    elif xx and x:
        if x.isdigit():
            await e.client.send_message(
                e.chat_id, xx, schedule=timedelta(seconds=int(x))
            )
            await eod(e, "`Scheduled msg Succesfully`")
        else:
            try:
                z = await ban_time(e, x)
                await ultroid_bot.send_message(e.chat_id, xx, schedule=z)
                await eod(e, "`Scheduled msg Succesfully`")
            except BaseException:
                await eod(e, "`Incorrect Format`")
    else:
        return await eod(e, "`Incorrect Format`")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
