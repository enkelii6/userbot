from pyrogram import Client, filters
from config import api_id, api_hash

app = Client("val", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("stval") | filters.command("n"))
async def response(_, message):
    await message.reply("Ты будешь моей валентинкой?? (/y or /n)")

@app.on_message(filters.command("y"))
async def yes(_, message):
    await message.reply("УРААА Я ЛЮБЛЮ ТЕБЯ!!!")

if __name__ == '__main__':
    app.run()
