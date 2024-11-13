import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from pyrogram.errors import *
from pyrogram.types import *
from userbot.core.function.emoji import emoji
from userbot.config import *

from userbot import *
from pyrogram import Client, enums
from pyrogram.types import Message

absen = [
    "**Hadir Sayang**",
    "**Hadir Ryn**",
    "**Hadir Cintakuu**",
    "**Maaf ka habis nemenin ka Ryn**",
    "**Maaf ka habis disuruh Tuan Ryn**",
    "**Hadir Sayang**",
    "**Akuuuuhhh haaadiirrrr**",
    "**Hadir brother Aku**",
    "**Sokap bet lu**",
    "**Apasi Bawel**",
    "**Maaf Kak Abis Omekk**",
    "**Akhuuuu Hadiirrr Anettt Nich**",
    "**Hadir Ryn Gantengg**",
    "**Iyaa Pukhi Bising Ku Tengok**",
]

@ubot.on_message(filters.user(DEVS) & filters.command("pikachu", "") & ~filters.me)
async def _(client, message):
    await message.reply(choice(absen))
