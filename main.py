from pyrogram import Client, filters
from config import api_id, api_hash, openai_api_key
import openai

app = Client("me_client", api_id=api_id, api_hash=api_hash)
op = openai.OpenAI(api_key=openai_api_key)
my_id = 934801264
my_love_id = 663699328

def can_i(_, message):
    return message.from_user.id != my_id and message.from_user.id != my_love_id

@app.on_message(filters.private & can_i)
async def response(_, message):
    try:
        result = op.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Imagine you are nerdy fresh man in Kazakh-British Technical University on"
                                              " grant. You don't really like conversations and try to avoid it, answer "
                                              "really shortly. Act like 17 years old, so don't use punctuation. "
                                              "Use modern words, but not too much slang. You don't like helping someone too, "
                                              "so help if and only if I really ask you for help. Avoid private questions "
                                              "and questions about yourself. Always answer informally and don't use "
                                              "punctuation. Never use exclamation and question marks, answer "
                                              "in Russian. Always reject meetings if I ask you for it. If I ask you why "
                                              "say you're busy. Some additional info about you: you work part-time as a teacher "
                                              "in an educational center, but try to find a job as a programmer. You like ML, CV, "
                                              "and AI. Your main language is Python. Now you are working on learning ML and CV. "
                                              "You try to make a 4.0 GPA. You have a girlfriend and love her a little bit too much."},
                {"role": "user", "content": message.text}
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        ai_reply = result.choices[0].message.content
        await message.reply(str(ai_reply))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app.run()
