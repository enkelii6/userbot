from pyrogram import Client, filters
from config import api_id, api_hash

app = Client("tag", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("tag"))
async def tag(_, message):
    text = ''
    async for member in app.get_chat_members(message.chat.id):
        text += f'@{member.user.username} '
    await message.reply(text)

if __name__ == "__main__":
    app.run()
