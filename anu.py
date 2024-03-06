from pyrogram import Client
from config import api_id, api_hash

app = Client("stfu", api_id=api_id, api_hash=api_hash)

def filt(_, message):
    return message.from_user.id == 896156568

@app.on_message(filt)
async def response(_, message):
    await message.reply("Anuar is talking...")

if __name__ == '__main__':
    app.run()
