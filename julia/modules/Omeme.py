from julia import CMD_HELP
from bs4 import BeautifulSoup
import urllib
from julia import OWNER_ID
from julia import SUDO_USERS
from julia import tbot
import glob
import speedtest
from datetime import datetime
import io
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import re
from telegraph import upload_file
from telethon import events
from telethon.tl.types import MessageMediaPhoto
import cv2
import numpy as np
import PIL
from PIL import Image, ImageDraw
import pygments, os, asyncio, shutil, scapy, sys, requests, re, subprocess, urllib
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
import urllib.request
from faker import Faker as dc
import bs4
import html2text
from bing_image_downloader import downloader
from pymongo import MongoClient
from telethon import *
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *
import json
import urllib.request
from telegraph import Telegraph
import asyncio
import shlex
from typing import Tuple
from julia import *
from julia.Config import Config
from julia.events import register
import sys
from telethon import events
import asyncio
import traceback
import random
client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["missjuliarobot"]
approved_users = db.approve
from telethon.errors.rpcerrorlist import YouBlockedUserError
fnt = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
async def can_change_info(message):
    result = await tbot(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (isinstance(
        p, types.ChannelParticipantAdmin) and p.admin_rights.change_info)

@register(pattern="^/meme")
async def _(event):

    if event.fwd_from:

        return

    f = await event.reply("Thinking... 🤔")

    await asyncio.sleep(2)

    x = random.randrange(1, 30)

    if x == 1:

        await f.edit(
            "[To your teachers on failing you in all your papers confidently, every time...](https://telegra.ph/file/431d178780f9bff353047.jpg)",
            link_preview=True,
        )

    if x == 2:

        await f.edit(
            "[A shift from the mainstream darling, sweetheart, jaanu, and what not...](https://telegra.ph/file/6bbb86a6c7d2c4a61e102.jpg)",
            link_preview=True,
        )

    if x == 3:

        await f.edit(
            "[To the guy who's friendzone-ing you...](https://telegra.ph/file/8930b05e9535e9b9b8229.jpg)",
            link_preview=True,
        )

    if x == 4:

        await f.edit(
            "[When your friend asks for his money back...](https://telegra.ph/file/2df575ab38df5ce9dbf5e.jpg)",
            link_preview=True,
        )

    if x == 5:

        await f.edit(
            "[A bad-ass reply to who do you think you are?](https://telegra.ph/file/3a35a0c37f4418da9f702.jpg)",
            link_preview=True,
        )

    if x == 6:

        await f.edit(
            "[When the traffic police stops your car and asks for documents...](https://telegra.ph/file/52612d58d6a61315a4c3a.jpg)",
            link_preview=True,
        )

    if x == 7:

        await f.edit(
            "[ When your friend asks about the food he/she just cooked and you don't want to break his/her heart...](https://telegra.ph/file/702df36088f5c26fef931.jpg)",
            link_preview=True,
        )

    if x == 8:

        await f.edit(
            "[When you're out of words...](https://telegra.ph/file/ba748a74bcab4a1135d2a.jpg)",
            link_preview=True,
        )

    if x == 9:

        await f.edit(
            "[When you realize your wallet is empty...](https://telegra.ph/file/a4508324b496d3d4580df.jpg)",
            link_preview=True,
        )

    if x == 10:

        await f.edit(
            "[When shit is about to happen...](https://telegra.ph/file/e15d9d64f9f25e8d05f19.jpg)",
            link_preview=True,
        )

    if x == 11:

        await f.edit(
            "[When that oversmart classmate shouts a wrong answer in class...](https://telegra.ph/file/1a225a2e4b7bfd7f7a809.jpg)",
            link_preview=True,
        )

    if x == 12:

        await f.edit(
            "[When things go wrong in a big fat Indian wedding...](https://telegra.ph/file/db69e17e85bb444caca32.jpg)",
            link_preview=True,
        )

    if x == 13:

        await f.edit(
            "[A perfect justification for breaking a promise...](https://telegra.ph/file/0b8fb8fb729d157844ac9.jpg)",
            link_preview=True,
        )

    if x == 14:

        await f.edit(
            "[When your friend just won't stop LOL-ing on something silly you said...](https://telegra.ph/file/247fa54106c32318797ae.jpg)",
            link_preview=True,
        )

    if x == 15:

        await f.edit(
            "[When someone makes a joke on you...](https://telegra.ph/file/2ee216651443524eaafcf.jpg)",
            link_preview=True,
        )

    if x == 16:

        await f.edit(
            "[When your professor insults you in front of the class...](https://telegra.ph/file/a2dc7317627e514a8e180.jpg)",
            link_preview=True,
        )

    if x == 17:

        await f.edit(
            "[When your job interviewer asks if you're nervous...](https://telegra.ph/file/9cc147d0bf8adbebf164b.jpg)",
            link_preview=True,
        )

    if x == 18:

        await f.edit(
            "[When you're sick of someone complaining about the heat outside...](https://telegra.ph/file/9248635263c52b968f968.jpg)",
            link_preview=True,
        )

    if x == 19:

        await f.edit(
            "[When your adda is occupied by outsiders...](https://telegra.ph/file/ef537007ba6d9d4cbd384.jpg)",
            link_preview=True,
        )

    if x == 20:

        await f.edit(
            "[When you don't have the right words to motivate somebody...](https://telegra.ph/file/2c932d769ae4c5fbed368.jpg)",
            link_preview=True,
        )

    if x == 21:

        await f.edit(
            "[When the bouncer won't let you and your group of friends in because you're all under-aged...](https://telegra.ph/file/6c8ca79f1e20ebd04391c.jpg)",
            link_preview=True,
        )

    if x == 22:

        await f.edit(
            "[To the friend who wants you to take the fall for his actions...](https://telegra.ph/file/d4171b9bc9104b5d972d9.jpg)",
            link_preview=True,
        )

    if x == 23:

        await f.edit(
            "[When that prick of a bully wouldn't take your words seriously...](https://telegra.ph/file/188d73bd24cf866d8d8d0.jpg)",
            link_preview=True,
        )

    if x == 24:

        await f.edit(
            "[ When you're forced to go shopping/watch a football match with your partner...](https://telegra.ph/file/6e129f138c99c1886cb2b.jpg)",
            link_preview=True,
        )

    if x == 25:

        await f.edit(
            "[To the large queue behind you after you get the last concert/movie ticket...](https://telegra.ph/file/2423f213dd4e4282a31ea.jpg)",
            link_preview=True,
        )

    if x == 26:

        await f.edit(
            "[When your parents thought you'd fail but you prove them wrong...](https://telegra.ph/file/39cc5098466f622bf21e3.jpg)",
            link_preview=True,
        )

    if x == 27:

        await f.edit(
            "[A justification for not voting!](https://telegra.ph/file/87d475a8f9a8350d2450e.jpg)",
            link_preview=True,
        )

    if x == 28:

        await f.edit(
            "[When your partner expects you to do too many things...](https://telegra.ph/file/68bc768d36e08862bf94e.jpg)",
            link_preview=True,
        )

    if x == 29:

        await f.edit(
            "[When your friends cancel on the plan you made at the last minute...](https://telegra.ph/file/960b58c8f625b17613307.jpg)",
            link_preview=True,
        )

    if x == 30:

        await f.edit(
            "[For that friend of yours who does not like loud music and head banging...](https://telegra.ph/file/acbce070d3c52b921b2bd.jpg)",
            link_preview=True,
        )

client = tbot
@register(pattern="^/meme")
async def _(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    reply = await event.get_reply_message()
    download = await tbot.download_media(reply.media, path)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("danish.png", frame)
    danish = Image.open("danish.png")
    dark,python = danish.size
    cobra = f"""ffmpeg -f lavfi -i color=c=ffffff00:s={dark}x{python}:d=10 -loop 1 -i danish.png -filter_complex "[1]rotate=angle=PI*t:fillcolor=none:ow='hypot(iw,ih)':oh=ow[fg];[0][fg]overlay=x=(W-w)/2:y=(H-h)/2:shortest=1:format=auto,format=yuv420p" -movflags +faststart danish.mp4 -y"""                 
    await event.reply("```Processing ...```")
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cobra, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    await event.reply("```Uploading...```")
    await event.client.send_file(event.chat_id, "danish.mp4" , force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.mp4")
    os.remove("danish.png")
