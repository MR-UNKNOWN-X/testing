# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/MR-UNKNOWN-X/testing/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/MR-UNKNOWN-X/testing/blob/main/LICENSE/>.

# https://github.com/xditya/TeleBot/blob/master/telebot/plugins/mybot/pmbot/incoming.py
"""
Incoming Message(s) forwarder.
"""

from telethon import events

from . import *

# if incoming


@asst.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def on_new_mssg(event):
    incoming = event.raw_text
    who = event.sender_id
    if is_blacklisted(who):
        return
    # doesn't reply to that user anymore
    if incoming.startswith("/"):
        pass
    elif who == OWNER_ID:
        return
    else:
        xx = await event.forward_to(OWNER_ID)
        udB.set(str(xx.id), str(who))
