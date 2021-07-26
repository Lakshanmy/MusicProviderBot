from asyncio import QueueEmpty
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message

from VCsMusicBot.config import que
from VCsMusicBot.function.admins import set
from VCsMusicBot.helpers.channelmusic import get_chat_id
from VCsMusicBot.helpers.decorators import authorized_users_only
from VCsMusicBot.helpers.decorators import errors
from VCsMusicBot.helpers.filters import command
from VCsMusicBot.helpers.filters import other_filters
from VCsMusicBot.services.callsmusic import callsmusic
from VCsMusicBot.services.queues import queues


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("⚒ Admin cache refreshed.")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "paused"
    ):
        await message.reply_text("❗ __Nothing is playing.__")
    else:
        callsmusic.pause(chat_id)
        await message.reply_text("⏸ **Paused.**")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.active_chats) or (
        callsmusic.active_chats[chat_id] == "playing"
    ):
        await message.reply_text("❗ __Nothing is paused.__")
    else:
        callsmusic.resume(chat_id)
        await message.reply_text("⏯ **Resumed.**")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ __Nothing is streaming.__")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        await callsmusic.stop(chat_id)
        await message.reply_text("❌ __Stopped streaming.__")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("❗ __Nothing is playing to skip.__")
    else:
        queues.task_done(chat_id)
        if queues.is_empty(chat_id):
            await callsmusic.stop(chat_id)
        else:
            await callsmusic.set_stream(
                chat_id, 
                queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- **⏭ Skipped :** __{skip[0]}__\n- **▶ Now Playing :** __{qeue[0][0]}__")


@Client.on_message(filters.command("reload"))
@errors
async def admincache(client, message: Message):
    set(
        message.chat.id,
        [
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("✅ Admin List Updated. \n🔄 Bot Restarted. \n🔄 Assistant Restarted. \n♻️ YT Search Mode Reloaded. \n♻️ Music DL Mode Reloaded. \n♻️ VC Play Mode Reloaded. \n\n🤖 => __@UwMusicProviderBot__ \n🎙 => __@UwMusicProvider__ \n\n© **@UNLIMITEDworldTEAM**")