import discord

client = discord.Client()


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("할말")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
