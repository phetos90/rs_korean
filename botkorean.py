import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("hi"):
        await message.channel.send("hihi")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
