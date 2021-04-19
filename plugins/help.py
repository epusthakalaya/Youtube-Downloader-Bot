from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url"
        helptxt = f"powered by: https://t.me/epusthakalaya_bots"
    await message.reply_text(helptxt)
